from flask import render_template

from app import app


@app.errorhandler(404)
def erro_404(error):
    return render_template('404.jinja')