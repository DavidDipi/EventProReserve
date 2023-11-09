from flask import Blueprint
from flask import render_template, redirect, url_for
from functools import wraps
from flask_login import current_user

ini_blueprint = Blueprint('ini', __name__, url_prefix='/')

def redirect_if_authenticated(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            if current_user.rol == 1:
                return redirect(url_for('admin.admin_home'))
            elif current_user.rol == 2:
                return redirect(url_for('client.client_home'))
            # Añade más condiciones para otros roles si es necesario
        return func(*args, **kwargs)
    return decorated_function


@ini_blueprint.route('/')
@redirect_if_authenticated
def ini_home():
    return render_template('index.html')


