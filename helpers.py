# THIRD PARTY IMPORTS
from flask import request, redirect, url_for, flash, session
from flask.globals import g
from functools import wraps
import re

# LOCAL IMPORTS
import app


def login_required(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        if g.user is None:
            flash('Please, sign in first')
            return redirect(url_for('signin'))
        return view(*args, **kwargs)
    return wrapper


def redirect_if_loggedin(route='account'):
    def decorator(view):
        @wraps(view)
        def wrapper(*args, **kwargs):
            if session.get('customerid') is not None:
                return redirect(url_for(route))
            return view(*args, **kwargs)
        return wrapper
    return decorator


def commit_on_finish(f):
    """
    Adiciona aos objetos atraves da sintaxe 'yield [objeto]' e faz commit.
    """
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        value = None
        def innerwrapper():
            nonlocal value
            value = yield from f(self, *args, **kwargs)

        # Adiciona todos os objetos da funcao antes de fazer commit
        for model in innerwrapper():
            app.db.session.add(model)

        app.db.session.commit()
        return value
    return wrapper


def form_validated_or_page_with_errors(f):
    """
    Inicializa e valida o form.
    Se houver erros retorna a pagina com as mensagens de erro,
    se nao retorna a funcao com o form preenchido.
    """
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        form = kwargs.get('form') or self.FORM(request.form)
        if not form.validate():
            return self.get(form=form)
        
        kwargs['form'] = form
        return f(self, *args, **kwargs)
    return wrapper

class _Mask:
    EMAIL = r'(?<=[a-z]{2})\w+(?=@)'
    EMAIL_ANONYMIZATION = r'^\w+(?=@)'

    def __call__(self, data, show_begin=0, show_end=0, /, *,
            pattern=None, mask_char='*', n_mask_char=6):
        if data is None:
            return None
        if pattern is None:
            return data[:show_begin] + mask_char * n_mask_char \
                    + data[len(data) - show_end:]
        return re.sub(pattern, mask_char * n_mask_char, data)

mask = _Mask()


class SecretClient:
    """Dummy class for saving keys in a local file instead of Azure"""
    
    def __init__(self, file, *args, **kwargs):
        self.file = file
    
    def set_secret(self, customerid, key, **kwargs):
        with open(self.file, 'a') as f:
            f.write('%s;%s\n' % (customerid, key))
            
    def get_secret(self, customerid, version=None, **kwargs):
        with open('isolated_db_keys.txt') as file:
            for line in file:
                _cid, key = line.split(';')
                if _cid == customerid:
                    return key.rstrip()
            else:
                raise KeyError('No keys found in file %s '
                                'for customerid %s' % (self.file, customerid))
