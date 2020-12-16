# THIRD PARTY IMPORTS
from flask.globals import g

# LOCAL IMPORTS
from forms.account import CustomerPersonalInfoForm
from views.utils import MethodViewWrapper, RequiredLoginViewMixin


class AccountView(MethodViewWrapper, RequiredLoginViewMixin):
    """Tela para visualizar dados do Customer"""

    def get(self):
        form = CustomerPersonalInfoForm(obj=g.user)
        return super().get(form=form)
