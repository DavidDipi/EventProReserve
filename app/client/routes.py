from flask import render_template, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user
from . import client_blueprint
from functools import wraps
import app
import os
# from app.context_processors import inject_client_name

# Decorador personalizado para verificar la autorización
def client_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.rol != 2:
            flash('Debe iniciar sesión como cliente para acceder a esta página', 'warning')
            return redirect(url_for('users.login'))
        return func(*args, **kwargs)
    return decorated_function



@client_blueprint.route('/')
@client_required
def client_home():
    from app.models import Cliente, User
    # Asegura que el usuario esté autenticado

    

    

    pagina_actual = request.path
    client = app.models.Cliente.query.all()
    return render_template('home-client.html', pagina_actual = pagina_actual)


@client_blueprint.route('/my-events')
@client_required
def my_events():
    # Asegura que el usuario esté autenticado

    pagina_actual = request.path
    return render_template('/pages/my-events.html', pagina_actual = pagina_actual)


@client_blueprint.route('/new-event')
@client_required
def new_events():
    # Asegura que el usuario esté autenticado

    pagina_actual = request.path
    events = app.models.TypeEvents.query.all()
    cantPers = app.models.AmountPeople.query.all()
    return render_template('/pages/new-event.html', pagina_actual = pagina_actual, events = events, cantPers = cantPers)