# THIRD PARTY IMPORTS
from wtforms.fields import StringField
from wtforms_alchemy import ModelFormField, ClassMap
import sqlalchemy_utils as su

# LOCAL IMPORTS
from forms.base import ModelForm
from models.customers import Customers
from models.isolated.customer_personal_info import CustomerPersonalInfo


class CsrfTokenDisabled(ModelForm):
    """Because of duplication of tokens"""
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('csrf_enabled', False)
        super().__init__(*args, **kwargs)


class SigninForm(ModelForm):
    class Meta:
        model = CustomerPersonalInfo
        only = [
            'email',
            'password',
        ]
        unique_validator = None
        
class SignupForm(CsrfTokenDisabled):
    class Meta:
        model = Customers
        only = [
            'gender', 'age', 'income',
            'country', 'state',
        ]
        optional_validator = None
        
class CustomerPersonalInfoForm(ModelForm):
    class Meta:
        model = CustomerPersonalInfo
        only = [
            'email', 'phone', 'firstname', 'lastname',
            'zip', 'city', 'address1', 'address2',
            'creditcard', 'creditcardexpiration',
            'password',
        ]
        optional_validator = None
        type_map = ClassMap({su.EncryptedType: StringField})
    
    more = ModelFormField(SignupForm)
        
class UpdateAccountForm(SignupForm):
    class Meta:
        pass