# THIRD PARTY IMPORTS
from flask import redirect, abort
from flask.helpers import flash, url_for
from flask.globals import g

# LOCAL IMPORTS
from models.isolated.customer_personal_info import CustomerPersonalInfo
from forms.account import CustomerPersonalInfoForm, UpdateAccountForm
from helpers import SecreVault
from ..helpers import form_validated_or_page_with_errors
from ..utils import FormMethodView, MethodViewWrapper, RequiredLoginViewMixin
from . import signout


class AccountView(MethodViewWrapper, RequiredLoginViewMixin):
    """Tela para visualizar dados do Customer"""

    def get(self):
        form = CustomerPersonalInfoForm(obj=g.user)
        return super().get(form=form)


class AccountEdit(FormMethodView, RequiredLoginViewMixin):
    """Tela para visualizar dados do Customer"""

    FORM = UpdateAccountForm

    @form_validated_or_page_with_errors
    def post(self, form=None):
        customer = CustomerPersonalInfo.from_form(form)
        customer.save()
        return self.get(template=AccountView.TEMPLATE)


class AccountDelete(MethodViewWrapper, RequiredLoginViewMixin):
    """Rota para anonimizar Customer"""

    def get(self):
        if g.user is None:
            flash('Customer not found', category='error')
            abort(404)

        g.user.more.inactivated().save()
        g.user.delete()
        
        SecreVault.delete_key_id(g.user.customerid)

        flash("We're sorry to see you go :(")
        return redirect(url_for(signout.Signout.ROUTE))    
    