# THIRD PARTY IMPORTS
from flask.templating import render_template
from flask.views import MethodView

# LOCAL IMPORTS
from .helpers import login_required, redirect_if_loggedin
from .blueprint import app


class RequiredLoginViewMixin(MethodView):
    """Views que o login e obrigatorio"""

    decorators = (login_required,)


class RequiredLoggedoutViewMixin(MethodView):
    """
    Views que redirecionam a pagina conta se o usuario estiver logado
    """
    decorators = (redirect_if_loggedin('app.account'),)


class MethodViewWrapper(MethodView):

    def get(self, template=None, **kwargs):
        return render_template(template or self.TEMPLATE, **kwargs)

    @classmethod
    def as_view(cls, name, *class_args, **class_kwargs):
        """Adiciona parametros as classes rotas"""
        
        cls.ROUTE = getattr(cls, 'ROUTE', None) or 'app.' + name

        # Se a rota estiver separada por '.',
        # assumimos que o template esta em subpastas
        # na sequencia em que foi declarada
        cls.TEMPLATE = getattr(cls, 'TEMPLATE', None) or \
            name.replace('.', '/') + '.jinja' # app.config['APP_TEMPLATE_EXT']

        return super().as_view(name, *class_args, **class_kwargs)


class FormMethodView(MethodViewWrapper):
    """View que implementa o metodo get com FORM padrao"""

    def FORM(self):
        "Implementar como variavel que retorna uma classe Form"
        raise NotImplementedError('You need to override "FORM"!!')

    def get(self, template=None, form=None, **kwargs):
        return super().get(template, form=form or self.FORM(), **kwargs)
