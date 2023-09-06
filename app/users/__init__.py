from flask import Blueprint

users_blueprint = Blueprint('users', 
                            __name__, 
                            url_prefix='/',
                            template_folder='../templates')
 
# Vincular archivo de rutas
from . import routes