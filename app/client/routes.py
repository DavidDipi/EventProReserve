from flask import render_template, request, send_from_directory, flash, redirect, url_for
from flask_login import current_user
from datetime import datetime
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
    # client = app.models.Cliente.query.all()
    # Tipo de evento
    events = app.models.TypeEvents.query.all()
    # Cantidad de personas
    cantPers = app.models.AmountPeople.query.all()
    # Mobiliario adicional
    adMobs = app.models.AdditionalMob.query.all()
    # Active
    active = app.models.Est_Active.query.all()
    # Decoracion adicional
    adDecs = app.models.AdditionalDec.query.all()
    # Alimentos adicionales
    adAlis = app.models.AdditionalAli.query.all()
    # Servicios adicionales
    ots = app.models.OthersServ.query.all()
    return render_template('home-client.html', 
                           pagina_actual = pagina_actual,
                           events = events,
                           cantPers = cantPers,
                           adMobs = adMobs,
                           active = active,
                           adDecs = adDecs,
                           adAlis = adAlis,
                           ots = ots)


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


@client_blueprint.route('/c_event', methods=['POST'])
@client_required
def c_event():
    try:
        from app import db
        from app.models import EventsTbl
        data = request.json  # Ajusta esto según el formato de tus datos

        # Obtén la fecha y hora actuales
        fecha_actual = datetime.now()
        print(fecha_actual)
        idAct = 1

        print(fecha_actual)

        # Crea una instancia de EventsTbl y asigna los valores
        event = EventsTbl(
            idClient=data['idUser'],
            idTypeEvent=data['typeEvent'],
            idAmountPe=data['numberPerson'],
            idAdMob=data['dataMob'],
            idAdDec=data['dataDec'],
            idAdAli=data['dataAli'],
            idOtServ=data['others'],
            idAct=idAct,
            dateCreateCot=fecha_actual,
            dateRealizationEvent=fecha_actual.replace(hour=0, minute=0, second=0, microsecond=0)
        )

        # Agrega la instancia a la sesión y confirma los cambios
        db.session.add(event)
        db.session.commit()# Asumiendo que los datos se envían como JSON


        return redirect(url_for("events.listar_events"))
    except Exception as e:
        # Maneja cualquier error que pueda ocurrir durante el proceso
        print('Error al procesar y guardar datos:', str(e))
        return redirect(url_for("events.listar_events"))
