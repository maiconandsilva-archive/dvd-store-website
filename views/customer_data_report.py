#THIRD PARTY IMPORTS
from datetime import datetime
from views.utils import RequiredLoginViewMixin
from flask.globals import g
from flask.helpers import send_file
from flask.templating import render_template
from flask.views import MethodView

import os
import shutil

# LOCAL IMPORTS
from models.customers import Customers
from helpers import form_validated_or_page_with_errors, redirect_if_loggedin
from app import app


class CustomerDataReport(RequiredLoginViewMixin, MethodView):
    REPORT_NAME = 'Customer Data Report'
    TPL_BASE_DIR = 'report/customer_data/'
    TPL_EXT = app.config['APP_TEMPLATE_EXT']
    REPORT_PATH = app.config['REPORT_PATH']
    
    TPL_CUSTOMER_PROFILE = 'customer_profile'
    TPL_PURCHASING_HISTORY = 'purchasing_history'
    TPL_INDEX = 'index'
    
    TEMPLATES = [
        TPL_CUSTOMER_PROFILE,
        TPL_PURCHASING_HISTORY,
        TPL_INDEX,
    ]
        
    @property
    def archive_name(self):
        return f'{self.REPORT_NAME}_{datetime.now()}'
    
    @property    
    def path_report(self):
        return f'{self.REPORT_PATH}/{g.user.customerid}'
    
    def path_template(self, template):
        return self.TPL_BASE_DIR + template + self.TPL_EXT
    
    # @form_validated_or_page_with_errors
    def post(self):
        report_name = self.build_customer_data_report()
        return send_file(report_name, mimetype='zip', as_attachment=True)
        
    def build_customer_data_report(self):
        self.render_report(g.user, self.path_report)
        return shutil.make_archive(self.archive_name, 'zip', self.path_report)

    def render_report(self, customer, dir):
        os.makedirs(dir, exist_ok=True)
        for TPL in self.TEMPLATES:
            with open(f'{dir}/{TPL}.html', 'w') as f:
                f.write(render_template(self.path_template(TPL), user=customer))
        