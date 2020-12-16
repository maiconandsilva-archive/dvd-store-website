# THIRD PARTY IMPORTS
from flask import redirect
from flask.helpers import flash, url_for
from flask.globals import g, session
from sqlalchemy.inspection import inspect

# LOCAL IMPORTS
from helpers import SecreVault
from models.isolated.customer_personal_info import CustomerPersonalInfo
from forms.account import SigninForm
from ..helpers import form_validated_or_page_with_errors
from ..utils import FormMethodView, RequiredLoggedoutViewMixin
from . import account_view


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
                session['customerid'] = customer.customerid
                session['cryptkey'] = \
                    SecreVault.get_secret(customer.customerid).value
                return redirect(url_for(account_view.AccountView.ROUTE))
        
        flash("Email or Password doesn't match")
        return self.get(form=form)