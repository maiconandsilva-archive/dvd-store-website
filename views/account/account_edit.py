# THIRD PARTY IMPORTS
# LOCAL IMPORTS
from forms.account import CustomerPersonalInfoForm, UpdateAccountForm
from ..utils import FormMethodView, RequiredLoginViewMixin
from ..helpers import form_validated_or_page_with_errors
from . import account_view


class AccountEdit(FormMethodView, RequiredLoginViewMixin):
    """Tela para visualizar dados do Customer"""

    FORM = UpdateAccountForm

    @form_validated_or_page_with_errors
    def post(self, form=None):
        customer = CustomerPersonalInfoForm.from_form(form)
        customer.save()
        return self.get(template=account_view.AccountView.TEMPLATE)