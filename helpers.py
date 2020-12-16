# THIRD PARTY IMPORTS
from flask import session
from multiprocessing import Process
from collections import namedtuple
import re
import os

# LOCAL IMPORTS


__all__  = ['mask', 'SecreVault']

class Mask:
    def __init__(self):
        self.__p = {} # list of registered mask regex patterns

    def __call__(self, pattern_name, data, /, *, mask_char='*', n_mask_char=6):
        return data and re.sub(self.__p[pattern_name], mask_char * n_mask_char, data)
    
    def register(self, name, mask_pattern):
        self.__p[name] = mask_pattern

mask = Mask()
mask.register('EMAIL', r'(?<=[a-z]{2})\w+(?=@)')
mask.register('EMAIL_ANONYMIZATION', r'^\w+(?=@)')
mask.register('PHONE', r'(?<=\d{3}).+(?=\d{2})')


class SecretClient:
    """Dummy class for saving keys in a local file instead of Azure"""
    
    Secret =  namedtuple('Secret', ('value',))
    
    def __init__(self, file, *args, **kwargs):
        self.file = file

    def __idmatches(self, line, customerid):
        _cid_key = line.split(';')
        return (_cid_key[0] == customerid, *_cid_key)
        
    def set_secret(self, customerid, key, **kwargs):
        with open(self.file, 'a') as f:
            f.write('%s;%s\n' % (customerid, key))
    
    def get_secret(self, customerid, version=None, **kwargs):
        customerid = str(customerid)
        with open(self.file) as file:
            for line in file:
                idmatches, _cid, key = self.__idmatches(line, customerid)
                if idmatches:
                    return self.Secret(key.rstrip())
            else:
                raise KeyError('No keys found in file %s '
                                'for customerid %s' % (self.file, customerid))
    
    def begin_delete_secret(self, customerid, **kwargs):
        customerid = str(customerid)
        with open(self.file, 'r+') as file:
            alllines = file.readlines()
            file.seek(0)
            for line in alllines:
                if not self.__idmatches(line, customerid)[0]:
                    file.write(line)
            file.truncate()


class SecretVaultMeta(type):
    def __init__(self, name, bases, namespace):
        """
        If there is no configuration for Azure Key Vault, use a dummy class that
        writes key in file for development. No need to create an Azure account
        """
        from azure.identity import DefaultAzureCredential
        from azure.core.exceptions import ClientAuthenticationError
        import azure.keyvault.secrets as azure_secrets
        
        super().__init__(name, bases, namespace)
        
        try:        
            _vault_uri = os.environ['SECRET_VAULT_URI']
            _default_credential = DefaultAzureCredential()
            self.__client = \
                azure_secrets.SecretClient(_vault_uri, _default_credential)
            
        except (ImportError, KeyError, ValueError, ClientAuthenticationError):
            _vault_uri = os.environ['SECRET_VAULT_FILE_DEV']
            self.__client = SecretClient(_vault_uri)
            
    def __getattr__(self, attr):
        return getattr(self.__client, attr)


class SecreVault(metaclass=SecretVaultMeta):
    @classmethod
    def store_key_id(cls, customerid):
        """Store id;key on an isolated environment"""
        key = session['cryptkey'].decode()
        set_secret_task = Process(daemon=True,
            target=cls.set_secret, args=(customerid, key))
        set_secret_task.start()
    
    @classmethod
    def delete_key_id(cls, customerid):
        cls.begin_delete_secret(customerid)
