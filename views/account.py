# THIRD PARTY IMPORTS
from flask import redirect, abort
from flask.helpers import flash, url_for
from flask.globals import g, session
from sqlalchemy.inspection import inspect

# LOCAL IMPORTS
from helpers import (
    commit_on_finish, delete_key_id,
    form_validated_or_page_with_errors,
    store_key_id
)
from forms.account import CustomerPersonalInfoForm, SignupForm, SigninForm, UpdateAccountForm
from models.customers import Customers
from models.isolated.customer_personal_info import CustomerPersonalInfo
from views.utils import (FormMethodView, MethodViewWrapper,
    RequiredLoggedoutViewMixin, RequiredLoginViewMixin,
)
import app


class AccountEdit(FormMethodView, RequiredLoginViewMixin):
    """Tela para visualizar dados do Customer"""

    FORM = UpdateAccountForm

    @form_validated_or_page_with_errors
    @commit_on_finish
    def post(self, form=None):
        customer = CustomerPersonalInfo.from_form(form)
        yield customer
        return self.get(template=AccountView.TEMPLATE)


class AccountView(MethodViewWrapper, RequiredLoginViewMixin):
    """Tela para visualizar dados do Customer"""

    def get(self):
        form = CustomerPersonalInfoForm(obj=g.user)
        return super().get(form=form)


class AccountDelete(MethodViewWrapper, RequiredLoginViewMixin):
    """Rota para anonimizar Customer"""

    def get(self):
        if g.user is None:
            flash('Customer not found', category='error')
            abort(404)

        g.user.more.inactivated().save()
        g.user.delete()
        
        delete_key_id(g.user.customerid)

        flash("We're sorry to see you go :(")
        return redirect(url_for(Signout.ROUTE))

class Signin(FormMethodView, RequiredLoggedoutViewMixin):
    """Rota de login"""

    FORM = SigninForm
    
    @form_validated_or_page_with_errors
    def post(self, form=None):
        # Deactivate decryption for authentication
        g.allowdecryption = False
        
        customer = CustomerPersonalInfo.query.filter(
            CustomerPersonalInfo.email==form.email.data).one_or_none()
        
        if customer and customer.more.is_active:
            if customer.password == form.password.data:
                if inspect(customer).modified:
                    # If password was unencrypted, save new encrypted password
                    customer.save()
                session['customerid'] = customer.customerid
                session['cryptkey'] = \
                    app.secret_vault_client.get_secret(customer.customerid).value
                return redirect(url_for(AccountView.ROUTE))
        
        flash("Email or Password doesn't match")
        return self.get(form=form)


class Signup(FormMethodView, RequiredLoggedoutViewMixin):
    """Rota para registrar usuario"""

    FORM = CustomerPersonalInfoForm

    @form_validated_or_page_with_errors
    # @commit_on_finish
    def post(self, form=None):
        customer = CustomerPersonalInfo.from_form(form)
        
        customer.save()
        
        store_key_id(customer.customerid)

        flash('Thank You For Signing Up!')
        return redirect(url_for(Signin.ROUTE))


class Signout(MethodViewWrapper):
    """Rota para deslogar usuario"""

    def dispatch_request(self):
        session.clear()
        return redirect(url_for(Signin.ROUTE))
