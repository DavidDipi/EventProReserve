from flask import Flask, render_template, session
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_session import Session
from .mi_blueprint import ini_blueprint
from app.users import users_blueprint
from app.admin import admin_blueprint, admin_events_blueprint, admin_users_blueprint
from app.client import client_blueprint

# Crear el objeto de aplicación
app = Flask(__name__)
app.config.from_object(Config)

# Crear el objeto sqlalchemy
db = SQLAlchemy(app)
# Crear el objeto de migracion y activarlo
migrate = Migrate(app , db)

# Configurar session
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)


# Configurar bootstrap
bootstrap = Bootstrap(app)

# Registrar el nuevo modulo

app.register_blueprint(ini_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(admin_events_blueprint)
app.register_blueprint(admin_users_blueprint)
app.register_blueprint(client_blueprint)


# Traer modelos
from .models import TypeEvents, User, Cliente

