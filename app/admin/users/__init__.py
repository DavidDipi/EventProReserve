from flask import Blueprint

users = Blueprint('usersAdmin',
                        __name__,
                        url_prefix = '/admin/users',
                        template_folder = '../templates',
                        static_folder="img"
                    )

# Vincular el archivo de rutas
from . import routes