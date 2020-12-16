# THIRD PARTY IMPORTS
from flask import redirect
from flask.helpers import url_for
from flask.globals import session

# LOCAL IMPORTS
from ..utils import MethodViewWrapper
from . import signin


class Signout(MethodViewWrapper):
    """Rota para deslogar usuario"""

    def dispatch_request(self):
        session.clear()
        return redirect(url_for(signin.Signin.ROUTE))
