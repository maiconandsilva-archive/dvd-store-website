from flask import Flask, redirect, abort
from flask.helpers import flash, url_for
from flask.templating import render_template
from flask.globals import g, session, request
from flask.json import jsonify

from sqlalchemy import orm

from app import app, db
from helpers import (commit_on_finish, login_required,
    redirect_if_loggedin, form_validated_or_page_with_errors,
)
from forms.account import SignupForm, SigninForm, UpdateAccountForm
from models.customers import Customers
from views.utils import (FormMethodView, MethodViewWrapper,
    RequiredLoggedoutViewMixin, RequiredLoginViewMixin,
)


class AccountEdit(FormMethodView, RequiredLoginViewMixin):
    """Tela para visualizar dados do Customer"""

    FORM = UpdateAccountForm

    def get(self):
        # TODO:
        return super().get()

    @commit_on_finish
    @form_validated_or_page_with_errors
    def post(self, form=None):
        customer = Customers.from_form(form)
        yield customer # deletes customer
        return self.get(template=AccountView.TEMPLATE)


class AccountView(MethodViewWrapper, RequiredLoginViewMixin):
    """Tela para visualizar dados do Customer"""

    def get(self):
        # TODO:
        form = UpdateAccountForm(obj=g.user)
        del form.password
        del form.username
        return super().get(form=form)


class AccountDelete(MethodViewWrapper, RequiredLoginViewMixin):
    """Rota para anonimizar Customer"""

    @commit_on_finish
    def get(self):
        if g.user is None:
            flash('Customer not found', category='error')
            abort(404)

        yield g.user.anonymized()

        flash("We're sorry to see you go :(")
        return redirect(url_for(Signout.ROUTE))
    

class Signin(FormMethodView, RequiredLoggedoutViewMixin):
    """Rota de login"""

    FORM = SigninForm
    
    @form_validated_or_page_with_errors
    def post(self, form=None):
        try:
            customer = Customers.query.filter(
                Customers.email==form.email.data).one() #TODO: one_or_none
            if customer.is_active:
                if customer.password == form.password.data:
                    session['customerid'] = customer.customerid
                    return redirect(url_for(AccountView.ROUTE))
        except orm.exc.NoResultFound:
            pass
        
        flash("Email or Password doesn't match")
        return self.get(form=form)


class Signup(FormMethodView, RequiredLoggedoutViewMixin):
    """Rota para registrar usuario"""

    FORM = SignupForm

    @commit_on_finish
    @form_validated_or_page_with_errors
    def post(self, form=None):
        # TODO: Verify if username doesn't exist already
        customer = Customers.from_form(form)
        
        # FIXME: Bug when form has errors
        yield customer

        flash('Thank You For Signing Up!')
        return redirect(url_for(Signin.ROUTE))


class Signout(MethodViewWrapper):
    """Rota para deslogar usuario"""

    def dispatch_request(self):
        session.clear()
        return redirect(url_for(Signin.ROUTE))
