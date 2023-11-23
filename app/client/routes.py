import traceback
from flask import render_template, request, make_response, flash, redirect, url_for, jsonify
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import DateField
from wtforms.validators import InputRequired
from datetime import datetime, timedelta
from . import client_blueprint
from functools import wraps
import app
import os
import pdfkit
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


# Formulario para la selección de fecha
class DateForm(FlaskForm):
    event_date = DateField('Event Date', validators=[InputRequired()], format='%Y-%m-%d')


@client_blueprint.route('/')
@client_required
def client_home():
    from app.models import Cliente, User, EventsTbl


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
    # Evento cotizado
    evts = app.models.EventsTbl.query.all()
    
    # SELECCIONAR FECHA
    
    form = DateForm()

    # Calcular la fecha mínima y máxima permitida
    min_date = datetime.now().date()
    max_date = min_date + timedelta(days=15)
    
    form.event_date.validators[0].min = max_date

    if form.validate_on_submit():
        selected_date = form.event_date.data
        # Aquí puedes hacer lo que necesites con la fecha seleccionada
        return f"Fecha seleccionada: {selected_date}"


    idUsuario = current_user.idUser  # Reemplaza esto con el ID del usuario específico
    ult_evts = EventsTbl.query.filter_by(idUser = idUsuario).order_by(EventsTbl.idEvent.desc()).first()
    return render_template('home-client.html', 
                           pagina_actual = pagina_actual,
                           events = events,
                           cantPers = cantPers,
                           adMobs = adMobs,
                           active = active,
                           adDecs = adDecs,
                           adAlis = adAlis,
                           ots = ots,
                           ult_evts = ult_evts,
                           form=form)


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
    from app.models import EventsTbl
    from app.models import db
    import traceback
    try:
        data = request.json  # Adjust this based on your data format
        print(data)
        print('Datos recibidos en el servidor:', data)

        # Get the current date and time
        fecha_actual = datetime.now()
        print(fecha_actual)
        idAct = 1

        print('idClient:', data['idUser'])

        # Create an instance of EventsTbl and save it to the database
        event = EventsTbl(
            idUser=data['idUser'],
            idTypeEvent=data['typeEvent'],
            idAmountPe=data['numberPerson'],
            adMob = data['dataMob'],
            adDec = data['dataDec'],
            adAli = data['dataAli'],
            otServ = data['others'],

            # Add other fields as needed
            idAct=idAct,
            dateCreateCot=fecha_actual,
            dateRealizationEvent=None
        )

        db.session.add(event)
        db.session.commit()

        return jsonify({'message': 'Datos recibidos y guardados correctamente'})
    except Exception as e:
        # Maneja cualquier error que pueda ocurrir durante el proceso
        print('Error al procesar y guardar datos:', str(e))
        traceback.print_exc()
        return jsonify({'message': 'Ocurrio un error'})


@client_blueprint.route("/e_event/<id>", methods=["POST"])
@client_required
def e_event(id):
    try:
        from app.models import EventsTbl
        from app import db
        data = request.form

        # Asegúrate de validar y manejar adecuadamente el caso en el que event_id sea None o esté vacío
        print(data)
        # Obtiene el evento a través del ID
        evento_a_actualizar = EventsTbl.query.get(id)
        print(evento_a_actualizar)

        if 'dateSelect' in data:
            fecha_str = data['dateSelect']
            
            try:
                # Convertir la cadena a un objeto datetime
                fecha_datetime = datetime.strptime(fecha_str, '%Y-%m-%d')
                
                # Actualizar los campos con la fecha convertida
                evento_a_actualizar.dateRealizationEvent = fecha_datetime
            except ValueError as e:
                # Manejar errores relacionados con el formato de fecha
                return jsonify({'message': 'Error en el formato de la fecha: ' + str(e)})

        print(fecha_datetime)
        # Actualiza los campos necesarios
        evento_a_actualizar.idTypeEvent = data['typeEvent']
        print(data['typeEvent'])
        evento_a_actualizar.idAmountPe = data['numberPerson']
        print(data['numberPerson'])
        evento_a_actualizar.otServ = data['others']
        print(print(fecha_datetime))

        # Guarda los cambios en la base de datos
        app.db.session.commit()

        return jsonify({'message': 'Datos actualizados correctamente'})
    except Exception as e:
        # Maneja cualquier error que pueda ocurrir durante el proceso
        traceback.print_exc()
        return jsonify({'message': 'Error al actualizar datos: ' + str(e)})
    

@client_blueprint.route("/get_date", methods=["POST"])
@client_required
def get_date():
    dateEvent = app.models.EventsTbl.query.all()
    list_dateEvent = []
    
    for date in dateEvent:
        fecha_string = date.dateRealizationEvent 
        
        # Convertir la cadena a objeto datetime

        
        fecha_formateada = str(fecha_string)
        
        list_dateEvent.append({
            "value": fecha_formateada,
        })

    return jsonify({'dateEvent': list_dateEvent})

@client_blueprint.route('/send_data_template',)


@client_blueprint.route('/generate_pdf/<id>', methods=['GET'])
@client_required
def generate_pdf(id):
    # Obtener los datos del evento desde la base de datos o donde los tengas almacenados
    # ...
    id_user = current_user.idUser
    id_event = id
    # Renderizar la plantilla HTML con los datos del evento
    rendered_template = render_template('pages/event_template.html', id=id)

    # Convertir el HTML a PDF utilizando pdfkit
    pdf_content = pdfkit.from_string(rendered_template, False)

    # Crear una respuesta de Flask con el contenido del PDF
    response = make_response(pdf_content)
    response.mimetype = 'application/pdf'
    response.headers['Content-Disposition'] = f'attachment; filename=event_report_client_{id_user}_event_{id_event}.pdf'

    return response
