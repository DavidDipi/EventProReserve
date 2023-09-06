from flask import Blueprint

client_blueprint = Blueprint('client', 
                            __name__, 
                            url_prefix='/client',
                            template_folder='templates')

 
# Vincular archivo de rutas
from . import routes