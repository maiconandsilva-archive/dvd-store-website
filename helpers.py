from flask import request, redirect, url_for, flash, session
from functools import partial, wraps

from flask.globals import g

from app import db

import re


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
            db.session.add(model)

        db.session.commit()
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