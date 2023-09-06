from flask import Blueprint
from flask import render_template

ini_blueprint = Blueprint('ini', __name__, url_prefix='/')

@ini_blueprint.route('/')
def ini_home():
    return render_template('index.html')


