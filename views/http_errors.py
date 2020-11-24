from flask import render_template

from app import app


@app.errorhandler(404)
def erro_404(error):
    return render_template('http_errors/404.jinja')

@app.errorhandler(500)
def erro_500(error):
    return render_template('http_error/500.jinja')
