from flask import render_template, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user
from . import client_blueprint
import app
import os
# from app.context_processors import inject_client_name




@client_blueprint.route('/')
def client_home():
    from app.models import Cliente, User
    # Asegura que el usuario esté autenticado
    if not current_user.is_authenticated:
        flash('Debe iniciar sesión para acceder a esta página', 'warning')
        return redirect(url_for('users.login'))
    
    # Obtiene el usuario autenticado
    usuario_actual = current_user
    
    # Obtiene el cliente asociado al usuario actual
    cliente = Cliente.query.filter_by(idUser=usuario_actual.idUser).first()
    
    # Accede a los datos del usuario y cliente
    nombre_usuario = usuario_actual.emailUser  # Ajusta esto según tu modelo de Usuario
    nombre_cliente = cliente.fullnameClient
    

    pagina_actual = request.path
    client = app.models.Cliente.query.all()
    return render_template('home-client.html', pagina_actual = pagina_actual, nombre_cliente = nombre_cliente)

@client_blueprint.route('/my-events')
def my_events():
    # Asegura que el usuario esté autenticado
    if not current_user.is_authenticated:
        flash('Debe iniciar sesión para acceder a esta página', 'warning')
        return redirect(url_for('users.login'))
    pagina_actual = request.path
    return render_template('/pages/my-events.html', pagina_actual = pagina_actual)

@client_blueprint.route('/new-event')
def new_events():
    # Asegura que el usuario esté autenticado
    if not current_user.is_authenticated:
        flash('Debe iniciar sesión para acceder a esta página', 'warning')
        return redirect(url_for('users.login'))
    pagina_actual = request.path
    events = app.models.TypeEvents.query.all()
    return render_template('/pages/new-event.html', pagina_actual = pagina_actual, events = events)