# THIRD PARTY IMPORTS
from flask_sqlalchemy import SQLAlchemy

# LOCAL IMPORTS
import models.base


db = SQLAlchemy(model_class=models.base.BaseModel)