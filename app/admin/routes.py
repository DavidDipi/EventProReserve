from flask import render_template, request, send_from_directory
from . import admin_blueprint
import app
import os

@admin_blueprint.route('/')
def admin_home():
    from app.models import Cliente
    pagina_actual = request.path
    total_clients = Cliente.query.count()
    return render_template('home.html', 
                           pagina_actual = pagina_actual,
                           total_clients = total_clients)

@admin_blueprint.route('/static/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('static/css', filename)