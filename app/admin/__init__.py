# En admin_routes.py
from flask import Blueprint
from app.admin.events import events
from app.admin.users import users

admin_blueprint = Blueprint('admin', 
                            __name__, 
                            url_prefix='/admin',
                            template_folder='templates')

# Exportar el blueprint 'events'
admin_events_blueprint = events
admin_users_blueprint = users
 
# Vincular archivo de rutas
from . import routes