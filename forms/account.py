# THIRD PARTY IMPORTS

# LOCAL IMPORTS
from forms.base import ModelForm
from models.customers import Customers


class SigninForm(ModelForm):
    class Meta:
        model = Customers
        only = [
            'email',
            'password',
        ]
        unique_validator = None


class SignupForm(ModelForm):
    class Meta:
        model = Customers
        only = [
            'email', 'phone', 'firstname', 'lastname',
            'gender', 'age', 'income',
            'country', 'zip', 'city', 'state',
            'address1', 'address2',
            'creditcard', 'creditcardexpiration',
            'username', 'password',
        ]

class UpdateAccountForm(SignupForm):
    class Meta:
        pass