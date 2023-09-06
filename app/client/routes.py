from flask import render_template, request, send_from_directory
from . import client_blueprint
import app
import os

@client_blueprint.route('/')
def client_home():
    pagina_actual = request.path
    return render_template('home-client.html', pagina_actual = pagina_actual)