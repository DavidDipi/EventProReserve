import traceback
from flask import render_template, request, make_response, flash, redirect, url_for, jsonify,send_file
from flask_login import current_user
from flask_wtf import FlaskForm
import jinja2
from wtforms import DateField
from wtforms.validators import InputRequired
from datetime import datetime, timedelta
from . import client_blueprint
from functools import wraps
from sqlalchemy import func
import app
import os
import pdfkit
# from flask_wkhtmltopdf import Wkhtmltopdf
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
    print(ult_evts)
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


def crea_pdf(ruta_template, info, id_event, rutacss='C:/Users/David/Desktop/mirvaj-python/app/static/css/bootstrap.min.css'):
    nombre_template = ruta_template.split('/')[-1]
    ruta_template = ruta_template.replace(nombre_template, '')
    
    template_loader = jinja2.FileSystemLoader('app/client/templates/pages/')
    env = jinja2.Environment(loader=template_loader)
    html_template = 'bill.html' 
    template = env.get_template(html_template)
    html = template.render(info)
    
    options = {
        'page-size': 'Letter',
        'orientation': 'Portrait',
        'encoding': 'UTF-8',
        'enable-local-file-access': ''
    }
    
    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    id_str = str(id_event)
    print(id_str)
    ruta_salida = f'C:/Users/David/Desktop/mirvaj-python/app/static/pdfs/bill{id_str}.pdf'
    attachment_filename=f'bill{id_str}.pdf'
    pdfkit.from_string(html, ruta_salida, css=rutacss, options=options, configuration=config)
    
    descargar_pdf(ruta_salida=ruta_salida, id_event=id_event)
    
def descargar_pdf(ruta_salida, id_event):
    id_str = str(id_event)
    nombre_archivo = f'bill{id_str}.pdf'
    return send_file(ruta_salida, as_attachment=True, attachment_filename=nombre_archivo)
    


@client_blueprint.route('/generate_pdf/<id>', methods=['GET'])
@client_required
def generate_pdf(id):
    from app.models import EventsTbl, TypeEvents, Est_Active, User, AmountPeople, AdditionalMob, AdditionalDec, AdditionalAli, OthersServ, Cliente
    
    print(f"ID del evento: {id}")
    

    # Realiza la consulta uniéndote a las tablas relacionadas por claves foráneas
    event_data = app.db.session.query(
        EventsTbl,
        func.coalesce(User.emailUser, ''),
        func.coalesce(TypeEvents.nameTypeEvent, ''),
        func.coalesce(Est_Active.estAct, ''),
        func.coalesce(AmountPeople.AmountPe, ''),
        func.coalesce(AmountPeople.costAmountPe, ''),
        func.coalesce(EventsTbl.adMob, ''),  # Manejar el valor nulo para adMob
        func.coalesce(EventsTbl.adDec, ''),  # Manejar el valor nulo para adDec
        func.coalesce(EventsTbl.adAli, ''),  # Manejar el valor nulo para adAli
        func.coalesce(EventsTbl.otServ, ''),  # Manejar el valor nulo para otServ
        EventsTbl.dateCreateCot,
        EventsTbl.dateRealizationEvent,
        Cliente.fullnameClient,
        Cliente.phoneClient
    ).join(User, EventsTbl.idUser == User.idUser)\
    .join(TypeEvents, EventsTbl.idTypeEvent == TypeEvents.idTypeEvent)\
    .join(Est_Active, EventsTbl.idAct == Est_Active.idAct)\
    .join(AmountPeople, EventsTbl.idAmountPe == AmountPeople.idAmountPe)\
    .join(Cliente, User.idUser == Cliente.idUser)\
    .filter(EventsTbl.idEvent == 6)\
    .first()
    
    print(event_data)

    if event_data:
        event, user_email, type_event_name, est_active, amount_people, cost_aPeople, adMob, adDec, adAli, otServ, date_create_cot, date_realization_event, client_fullname, client_phone = event_data
        
        # Separar los datos de texto en ID y cantidad
        ad_mob_data = split_text_multiple(event.adMob)
        ad_dec_data = split_text_multiple(event.adDec)
        ad_ali_data = split_text_multiple(event.adAli)
        
        def get_costs(ids_list, model, id_column, cost_column_name, name_column):
            costs = []
            names = []
            for ids in ids_list:
                cost = 0
                name_list = []
                cost_list = []
                for id_value, quantity in zip(ids[0], ids[1]):
                    cost = app.db.session.query(getattr(model, cost_column_name)).filter(getattr(model, id_column) == id_value).scalar() or 0
                    name = app.db.session.query(getattr(model, name_column)).filter(getattr(model, id_column) == id_value).scalar() or ''
                    name_list.append(name)
                    cost_list.append(cost * int(quantity))
                costs.append(cost_list)
                names.append(name_list)
            return costs, names


        # Obtener los costos para cada campo
        ad_mob_costs, ad_mob_names = get_costs(ad_mob_data, AdditionalMob, 'idAdMob', 'costAdMob', 'nameAdMob')
        ad_dec_costs, ad_dec_names = get_costs(ad_dec_data, AdditionalDec, 'idAdDec', 'costAdDec', 'nameAdDec')
        ad_ali_costs, ad_ali_names = get_costs(ad_ali_data, AdditionalAli, 'idAdAli', 'costAdAli', 'nameAdAli')
        ot_serv_name = app.db.session.query(OthersServ.nameOtServ).filter(OthersServ.idOtServ == event.otServ).scalar() or ''
        ot_serv_cost = app.db.session.query(OthersServ.costOtServ).filter(OthersServ.idOtServ == event.otServ).scalar() or 0


        ad_mob_combined = list(zip(ad_mob_names, ad_mob_costs))
        ad_dec_combined = list(zip(ad_dec_names, ad_dec_costs))
        ad_ali_combined = list(zip(ad_ali_names, ad_ali_costs))
        
        # Convertir cost_aPeople a un número (si es una cadena)
        cost_aPeople = int(cost_aPeople)
        
        # Suma de cada lista de costos individuales
        total_ad_mob_cost = sum(sum(ad_mob) for ad_mob in ad_mob_costs)
        total_ad_dec_cost = sum(sum(ad_dec) for ad_dec in ad_dec_costs)
        total_ad_ali_cost = sum(sum(ad_ali) for ad_ali in ad_ali_costs)
        
        priceTotal = total_ad_mob_cost + total_ad_dec_cost + total_ad_ali_cost + cost_aPeople
        
        print(priceTotal)

        # Aquí puedes trabajar con los datos obtenidos
        # Por ejemplo, imprimir los nombres relacionados a cada tabla
        context = {
            'event_id': event.idEvent,
            'user_email': user_email,
            'type_event_name': type_event_name,
            'est_active': est_active,
            'amount_people': amount_people,
            'ad_mob_name': ad_mob_names,
            'ad_dec_name': ad_dec_names,
            'ad_ali_name': ad_ali_names,
            'ad_mob_costs': ad_mob_costs,
            'ad_dec_costs': ad_dec_costs,
            'ad_ali_costs': ad_ali_costs,
            'ad_mob_combined': ad_mob_combined,
            'ad_dec_combined': ad_dec_combined,
            'ad_ali_combined': ad_ali_combined,
            'ot_serv_name': ot_serv_name,
            'ot_serv_cost': ot_serv_cost,
            'date_create_cot': date_create_cot,
            'date_realization_event': date_realization_event,
            'client_fullname': client_fullname,
            'client_phone': client_phone,
            'priceTotal': priceTotal
        }
        """
        # Obtener el texto del archivo HTML
        template_loader = jinja2.FileSystemLoader('app/client/templates/pages/')
        template_env = jinja2.Environment(loader=template_loader)
        html_template = 'bill.html' 
        template = template_env.get_template(html_template)
        output_text = template.render(context)
        
        
        # Crea una instancia de WKHtmlToPdf
        pdf_converter = Wkhtmltopdf()
        
        config = {
            'page-size': 'A4',
            'orientation': 'Landscape'
        }
        
        event_str = str(event)  
        # Convertir el archivo HTML a PDF
        pdf_converter.add_input_string(output_text)
        pdf_converter.render(output_file='bill' + event_str + '.pdf', options=config)"""
        
        ruta_template='app/client/templates/pages/bill.html'
        
        crea_pdf(ruta_template=ruta_template,info=context, id_event=event.idEvent)
    
    else:
        return render_template('pages/error.html')
    
    
def split_text_multiple(text):
    data_pairs = []
    if text and ';' in text:
        pairs = text.split(';')
        ids = []
        quantities = []
        for pair in pairs:
            id_value, *quantity = pair.split(':')
            if quantity:
                ids.append(id_value)
                quantities.append(quantity[0])  # Tomamos solo el primer valor si hay más de uno
        data_pairs.append((ids, quantities))
    return data_pairs


