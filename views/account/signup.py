# THIRD PARTY IMPORTS
from flask import redirect
from flask.helpers import flash, url_for

# LOCAL IMPORTS
from models.isolated.customer_personal_info import CustomerPersonalInfo
from forms.account import CustomerPersonalInfoForm
from helpers import SecreVault
from ..utils import FormMethodView, RequiredLoggedoutViewMixin
from ..helpers import form_validated_or_page_with_errors
from . import signin


class Signup(FormMethodView, RequiredLoggedoutViewMixin):
    """Rota para registrar usuario"""

    FORM = CustomerPersonalInfoForm

    @form_validated_or_page_with_errors
    def post(self, form=None):
        customer = CustomerPersonalInfo.from_form(form)
        customer.save()
        SecreVault.store_key_id(customer.customerid)

        flash('Thank You For Signing Up!')
        return redirect(url_for(signin.Signin.ROUTE))