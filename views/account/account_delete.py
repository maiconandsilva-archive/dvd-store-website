# THIRD PARTY IMPORTS
from flask import redirect, abort
from flask.globals import g
from flask.helpers import flash, url_for

# LOCAL IMPORTS
from helpers import SecreVault
from ..utils import MethodViewWrapper, RequiredLoginViewMixin
from .signout import Signout


class AccountDelete(MethodViewWrapper, RequiredLoginViewMixin):
    """Rota para anonimizar Customer"""

    def get(self):
        if g.user is None:
            flash('Customer not found', category='error')
            abort(404)

        g.user.more.inactivated().save()
        g.user.delete()
        
        SecreVault.delete_key_id(g.user.customerid)

        flash("We're sorry to see you go :(")
        return redirect(url_for(Signout.ROUTE))