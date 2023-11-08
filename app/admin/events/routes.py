from flask import render_template, request, jsonify, url_for, redirect, flash
from . import events
import app
from .forms_events import RegistrarTipoEvento
import os

# Rutas del modulo "EVENTOS"

# Listar y agregar tipos de eventos

@events.route("/", methods=["GET", "POST"])
def listar_events():
    pagina_actual = request.path
    
    # Agregar evento
    form = RegistrarTipoEvento()
    # Objeto vacío
    p = app.models.TypeEvents()
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.add(p)
        app.db.session.commit()
        
        response = {
            "status": "success",
            "message": "Evento registrado"
        }

        return redirect(url_for("events.listar_events")) 
    
    # Listar eventos
    events = app.models.TypeEvents.query.all()
    # Listar cantidad de personas
    amountPers = app.models.AmountPeople.query.all()
    # Listar mobiliario adicional
    adMobs = app.models.AdditionalMob.query.all()
    # Listar active
    active = app.models.Est_Active.query.all()
    return render_template ("/pages/events.html", 
                            events = events, 
                            pagina_actual = 
                            pagina_actual, 
                            form = form, 
                            amountPers = amountPers,
                            adMobs = adMobs,
                            active = active)


# Editar tipos de eventos
@events.route("/edit_event/<id>", methods=["GET", "POST"])
def edit_event(id):
    if request.method == "POST":
        p = app.models.TypeEvents()
        event = p.query.get(id)
        event.nameTypeEvent = request.form["nameTypeEvent"]
        event.descriptionTypeEvent = request.form["descriptionTypeEvent"]
        
        app.db.session.commit()
        
        return redirect(url_for("events.listar_events"))
    p = app.models.TypeEvents()
    event = p.query.get(id)
    return render_template("/pages/editEvent.html", event = event)


# Borrar tipos de eventos
@events.route("/delete_event/<id>", methods=["POST"])
def delete_event(id):
    p = app.models.TypeEvents()
    event_to_delete = p.query.get(id)  # Load the event from the database
    if event_to_delete:
        app.db.session.delete(event_to_delete)
        app.db.session.commit()
    return redirect(url_for("events.listar_events"))


# CREAR REGISTRO CANTIDAD DE PERSONAS
@events.route("/c_cant_pers", methods=["POST"])
def agg_cant_pers():
    from app.models import AmountPeople
    from app import db
    
    if request.method == 'POST':
    
        _AmountPe = request.form['cantPersons']
        _costAmountPe = request.form['costPersons']
    
        # Verificar que no existe la misma cantidad de personas
        existing_cantPer = AmountPeople.query.filter_by( AmountPe = _AmountPe ).first()
    
        
        if existing_cantPer:
            flash('Esta cantidad de personas ya esta registrada', 'error')
        else:   
            _cost_pers = request.form['costPersons']
            _estAct = request.form['state']
            
            cantPers = app.models.User()
            
            try:
                cantPers = AmountPeople( AmountPe = _AmountPe, costAmountPe = _cost_pers, idAct = _estAct )
                
                db.session.add(cantPers)
                db.session.commit()

                flash('Registro exitoso', 'success')
                
                return redirect(url_for("events.listar_events"))
            except Exception as e:
                # Manejar cualquier excepción que pueda ocurrir durante la inserción
                flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for("events.listar_events"))


# EDITAR REGISTRO CANTIDAD DE PERSONAS
@events.route("/e_cant_pers/<id>", methods=["POST"])
def e_cant_pers(id):
    
    AmountPe = request.form["AmountPe"]
    costAmountPe = request.form["costAmountPe"]
    active = request.form['state']
    
    if AmountPe == '' or costAmountPe == '':
        flash('Registro no valido', 'error')
        return redirect(url_for("events.listar_events"))
    else:
        p = app.models.AmountPeople()
        cantPers = p.query.get(id)
        cantPers.AmountPe = AmountPe
        cantPers.costAmountPe = costAmountPe
        cantPers.idAct = active
        
        app.db.session.commit()
        
        return redirect(url_for("events.listar_events"))

# BORRAR REGISTRO CANTIDAD DE PERSONAS
@events.route("/d_cant_pers/<id>", methods=["POST"])
def d_cant_pers(id):
    p = app.models.AmountPeople()
    d_cant_pers = p.query.get(id)  # Load the event from the database
    if d_cant_pers:
        app.db.session.delete(d_cant_pers)
        app.db.session.commit()
    return redirect(url_for("events.listar_events"))


# CREAR REGISTRO MOBILIARIO ADICIONAL
@events.route("/c_ad_mob", methods=["POST"])
def agg_ad_mob():
    from app.models import AdditionalMob
    from app import db
    
    if request.method == 'POST':
    
        _nameAdMob = request.form['nameMob']
    
        # Verificar que no existe el mismo mobiliario
        existing_adMob = AdditionalMob.query.filter_by( nameAdMob = _nameAdMob ).first()
    
        
        if existing_adMob:
            flash('Esta mobiliario ya esta registrado', 'error')
        else:   
            _costAdMob = request.form['costMob']
            _estAct = request.form['state']
                        
            try:
                p = AdditionalMob( nameAdMob = _nameAdMob, costAdMob = _costAdMob, idAct = _estAct )
                
                db.session.add(p)
                db.session.commit()

                flash('Registro exitoso', 'success')
                
                return redirect(url_for("events.listar_events"))
            except Exception as e:
                # Manejar cualquier excepción que pueda ocurrir durante la inserción
                flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for("events.listar_events"))


# EDITAR REGISTRO MOBILIARIO ADICIONAL
@events.route("/e_ad_mob/<id>", methods=["POST"])
def e_ad_mob(id):
    
    nameAdMob = request.form["nameAdMob"]
    costAdMob = request.form["costAdMob"]
    active = request.form['state']
    
    if nameAdMob == '' or costAdMob == '':
        flash('Registro no valido', 'error')
        return redirect(url_for("events.listar_events"))
    else:
        p = app.models.AdditionalMob()
        adMob = p.query.get(id)
        adMob.nameAdMob = nameAdMob
        adMob.costAdMob = costAdMob
        adMob.idAct = active
        
        app.db.session.commit()
        
        return redirect(url_for("events.listar_events"))
    
    
# BORRAR REGISTRO MOBILIARIO ADICIONAL
@events.route("/d_ad_mob/<id>", methods=["POST"])
def d_ad_mob(id):
    p = app.models.AdditionalMob()
    d_ad_mob = p.query.get(id)
    if d_ad_mob:
        app.db.session.delete(d_ad_mob)
        app.db.session.commit()
    else:
        flash('No se ha encontrado el registro a eliminar', 'error')
        
    return redirect(url_for("events.listar_events"))