#THIRD PARTY IMPORTS
from flask_talisman import Talisman
from time import sleep
import os

# LOCAL IMPORTS
from db import db


talisman = Talisman()


def create_tables(app):
    from models import orders, products, customers
    from models.isolated import customer_personal_info
    
    with app.app_context():
        print('Trying to connect to the database. Trial')
        
        for trial in range(1, 31):
            try:
                db.session.execute('SELECT 1')
                db.create_all()
                return
            except Exception as e:
                print(e)
            
            print(f' {trial}#', end='')
            sleep(2)


def init_debugger(app):
    """Initialize debugger if in debug environment"""
    if app.config.get('DEBUG'):
        import multiprocessing
        
        if multiprocessing.current_process().pid > 1:
            import debugpy

            debugpy.listen(('0.0.0.0', 10001))
            print('⏳ VS Code debugger can now be attached, '
                'press F5 in VS Code ⏳', flush=True)
            debugpy.wait_for_client()
            print('🎉 VS Code debugger attached, enjoy debugging 🎉', flush=True)