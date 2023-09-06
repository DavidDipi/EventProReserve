from flask import Blueprint

events = Blueprint('events',
                        __name__,
                        url_prefix = '/admin/events',
                        template_folder = '../templates',
                        static_folder="img"
                    )

# Vincular el archivo de rutas
from . import routes