from views.account import Signin
from flask.helpers import url_for
from werkzeug.utils import redirect
from .blueprint import app
 

@app.route('/')
def index():
    return redirect(url_for(Signin.ROUTE), code=302)