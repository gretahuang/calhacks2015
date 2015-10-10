import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager, Shell, Server
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from flask.ext.mail import Mail, Message
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

oid = OpenID(app, os.path.join(basedir, 'tmp'))
manager = Manager(app)
mail = Mail(app)

def make_shell_context():
    return dict(app=app, db=db, School=School, Student=Student, 
                Project=Project)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

from app import views, models

