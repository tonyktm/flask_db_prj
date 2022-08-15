from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from .routing import register_routes

app=Flask(__name__)


print(" * Loading default environment")

@app.route('/')
def hello():
    return "hello world...."

@app.route('/test')
def test_fun():
    return "This is a test function....**"



app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://dbuser1:rbu123@localhost:5432/testdb"
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)
ma = Marshmallow(app)



from app import models, controllers, helpers
from app.controllers import all_controller
from app.models import *

# register routes
#register_routes(app)
