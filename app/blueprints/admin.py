# En admin_routes.py
from flask import Blueprint
from flask import render_template, request



admin_blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@admin_blueprint.route('/')
def admin_home():
    pagina_actual = request.path
    return render_template('admin/home.html', pagina_actual = pagina_actual)
 