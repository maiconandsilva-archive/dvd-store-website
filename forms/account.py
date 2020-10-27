from forms import ModelForm
from models import Customers


class SigninForm(ModelForm):
    class Meta:
        model = Customers
        only = [
            'email',
            'password',
        ]


class SignupForm(ModelForm):
    class Meta:
        model = Customers
        only = [
            'firstname', 'lastname',
            'gender', 'age', 'income',
            'country', 'zip', 'city', 'state',
            'address1', 'address2',
            'creditcard', 'creditcardexpiration',
            'phone', 'username', 'email', 'password',
        ]

class UpdateAccountForm(SignupForm):
    class Meta:
        pass