# THIRD PARTY IMPORTS
from flask import request, redirect, url_for, flash, session
from flask.globals import g
from functools import wraps

# LOCAL IMPORTS
from extensions import db


def login_required(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        if g.user is None:
            flash('Please, sign in first')
            return redirect(url_for('app.signin'))
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
