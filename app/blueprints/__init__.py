"""from flask import Blueprint

# Crea los Blueprints
admin_blueprint = Blueprint('admin', __name__, url_prefix='/admin')
client_blueprint = Blueprint('client', __name__, url_prefix='/client')
ini_blueprint = Blueprint('ini', __name__, url_prefix='/')

# Importa las rutas desde los módulos
from . import admin_routes
from . import client_routes
from . import ini_routes

# Registra los Blueprints
admin_routes.register(admin_blueprint)
client_routes.register(client_blueprint)
ini_routes.register(ini_blueprint)"""