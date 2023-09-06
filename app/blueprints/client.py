# En admin_routes.py
from flask import Blueprint
from flask import render_template

client_blueprint = Blueprint('client', __name__, url_prefix='/client')

@client_blueprint.route('/')
def client_home():
    return render_template('client/home.html')