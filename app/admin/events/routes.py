from flask import  Flask, render_template, request, jsonify, url_for, redirect, flash
from . import events
from flask_login import current_user
from functools import wraps
import app
from .forms_events import RegistrarTipoEvento
import os

# Rutas del modulo "EVENTOS"

# Listar y agregar tipos de eventos

# Decorador personalizado para verificar la autorización
def admin_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.rol != 1:
            flash('Debe iniciar sesión como administrador para acceder a esta página', 'warning')
            return redirect(url_for('users.login'))
        return func(*args, **kwargs)
    return decorated_function


@events.route("/", methods=["GET", "POST"])
@admin_required
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
    # Listar decoracion adicional
    adDecs = app.models.AdditionalDec.query.all()
    # Listar alimentos adicionales
    adAlis = app.models.AdditionalAli.query.all()
    # Listar servicios adicionales
    ots = app.models.OthersServ.query.all()
    return render_template ("/pages/events.html", 
                            events = events, 
                            pagina_actual = 
                            pagina_actual, 
                            form = form, 
                            amountPers = amountPers,
                            adMobs = adMobs,
                            active = active,
                            adDecs = adDecs,
                            adAlis = adAlis,
                            ots = ots)


@events.route("/get_personas", methods=["POST"])
@admin_required
def get_person_datatable():
      # Listar eventos
       # Listar cantidad de personas
    amountPers = app.models.AmountPeople.query.all()
    list_pers = []
    for amountPer in amountPers:
        if(amountPer.idAct==1):
            estado="ACTIVO"
        else:
            estado="INACTIVO"

        list_pers.append({
            'id':amountPer.idAmountPe,
            'Cantidad':amountPer.AmountPe,
            'Costo':amountPer.costAmountPe,
            'Estado':estado
        })
    return jsonify({'pers':list_pers})


@events.route("/get_mobiliario", methods=["POST"])
@admin_required
def get_mobiliario_datatable():
      # Listar eventos
       # Listar cantidad de personas
    adMobs = app.models.AdditionalMob.query.all()
    list_adMobs = []
    for adMob in adMobs:
        if(adMob.idAct==1):
            estado="ACTIVO"
        else:
            estado="INACTIVO"


        list_adMobs.append({
            'id':adMob.idAdMob,
            'Nombre':adMob.nameAdMob,
            'Costo':adMob.costAdMob,
            'Estado':estado
        })
    return jsonify({'adMobs':list_adMobs})








@events.route("/get_event", methods=["POST"])
@admin_required
def get_event_datatable():
      # Listar eventos
    events = app.models.TypeEvents.query.all()
    list_event = []
    for event in events:
        if(event.idAct==1):
            estado="ACTIVO"
        else:
            estado="INACTIVO"

        list_event.append({
            'id':event.idTypeEvent,
            'Nombre':event.nameTypeEvent,
            'Descripción':event.descriptionTypeEvent,
            'Estado':estado
        })
    return jsonify({'events':list_event})



# CREAR REGISTRO TIPO DE EVENTO
@events.route("/c_tEvent", methods=["POST"])
@admin_required
def agg_tEvent():
    from app.models import TypeEvents
    from app import db
    
    if request.method == 'POST':
    
        _name = request.form['nameTypeEvent']
        
        existing = TypeEvents.query.filter_by( nameTypeEvent = _name ).first()
    
        
        if existing:
            flash('Esta registro ya esta registrado', 'error')
        else:   
            _description = request.form['descTypeEvent']
            _estAct = request.form['state']
            
            try:
                p = TypeEvents( nameTypeEvent = _name, descriptionTypeEvent = _description, idAct = _estAct )
                
                db.session.add(p)
                db.session.commit()

                flash('Registro exitoso', 'success')
                
                return redirect(url_for("events.listar_events"))
            except Exception as e:
                # Manejar cualquier excepción que pueda ocurrir durante la inserción
                flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for("events.listar_events"))

# Editar tipos de eventos
@events.route("/edit_event/<id>", methods=["GET", "POST"])
@admin_required
def edit_event(id):
    if request.method == "POST":
        p = app.models.TypeEvents()
        event = p.query.get(id)
        event.nameTypeEvent = request.form["nameTypeEvent"]
        event.descriptionTypeEvent = request.form["descriptionTypeEvent"]
        event.idAct = request.form["state"]
        
        app.db.session.commit()
        
        return redirect(url_for("events.listar_events"))
    p = app.models.TypeEvents()
    event = p.query.get(id)
    return render_template("/pages/editEvent.html", event = event)


# Borrar tipos de eventos
@events.route("/delete_event/<id>", methods=["POST"])
@admin_required
def delete_event(id):
    p = app.models.TypeEvents()
    event_to_delete = p.query.get(id)  # Load the event from the database
    if event_to_delete:
        app.db.session.delete(event_to_delete)
        app.db.session.commit()
    return redirect(url_for("events.listar_events"))


# CREAR REGISTRO CANTIDAD DE PERSONAS
@events.route("/c_cant_pers", methods=["POST"])
@admin_required
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
@admin_required
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
@admin_required
def d_cant_pers(id):
    p = app.models.AmountPeople()
    d_cant_pers = p.query.get(id)  # Load the event from the database
    if d_cant_pers:
        app.db.session.delete(d_cant_pers)
        app.db.session.commit()
    return redirect(url_for("events.listar_events"))


# CREAR REGISTRO MOBILIARIO ADICIONAL
@events.route("/c_ad_mob", methods=["POST"])
@admin_required
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
@admin_required
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
@admin_required
def d_ad_mob(id):
    p = app.models.AdditionalMob()
    d_ad_mob = p.query.get(id)
    if d_ad_mob:
        app.db.session.delete(d_ad_mob)
        app.db.session.commit()
    else:
        flash('No se ha encontrado el registro a eliminar', 'error')
        
    return redirect(url_for("events.listar_events"))


# CREAR REGISTRO DE DECORACION ADICIONAL
@events.route("/c_ad_dec", methods=["POST"])
@admin_required
def agg_ad_dec():
    from app.models import AdditionalDec
    from app import db
    
    if request.method == 'POST':
    
        _nameAdDec = request.form['nameDec']
    
        # Verificar que no existe el mismo decoracion
        existing_adDec = AdditionalDec.query.filter_by( nameAdDec = _nameAdDec ).first()
    
        
        if existing_adDec:
            flash('Esta decoracion ya esta registrado', 'error')
        else:   
            _costAdDec = request.form['costDec']
            _estAct = request.form['state']
                        
            try:
                p = AdditionalDec( nameAdDec = _nameAdDec, costAdDec = _costAdDec, idAct = _estAct )
                
                db.session.add(p)
                db.session.commit()

                flash('Registro exitoso', 'success')
                
                return redirect(url_for("events.listar_events"))
            except Exception as e:
                # Manejar cualquier excepción que pueda ocurrir durante la inserción
                flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for("events.listar_events"))


# EDITAR REGISTRO DE DECORACION ADICIONAL
@events.route("/e_ad_dec/<id>", methods=["POST"])
@admin_required
def e_ad_dec(id):
    
    nameAdDec = request.form["nameAdDec"]
    costAdDec = request.form["costAdDec"]
    active = request.form['state']
    
    if nameAdDec == '' or costAdDec == '':
        flash('Registro no valido', 'error')
        return redirect(url_for("events.listar_events"))
    else:
        p = app.models.AdditionalDec()
        adMob = p.query.get(id)
        adMob.nameAdDec = nameAdDec
        adMob.costAdDec = costAdDec
        adMob.idAct = active
        
        app.db.session.commit()
        
        return redirect(url_for("events.listar_events"))


# BORRAR REGISTRO DECORACION ADICIONAL
@events.route("/d_ad_dec/<id>", methods=["POST"])
@admin_required
def d_ad_dec(id):
    p = app.models.AdditionalDec()
    d_ad_dec = p.query.get(id)
    if d_ad_dec:
        app.db.session.delete(d_ad_dec)
        app.db.session.commit()
    else:
        flash('No se ha encontrado el registro a eliminar', 'error')
        
    return redirect(url_for("events.listar_events"))


# CREAR REGISTRO DE ALIMENTO ADICIONAL
@events.route("/c_ad_ali", methods=["POST"])
@admin_required
def agg_ad_ali():
    from app.models import AdditionalAli
    from app import db
    
    if request.method == 'POST':
    
        _name = request.form['nameAli']
        existing = AdditionalAli.query.filter_by( nameAdAli = _name ).first()
        
        
        if existing:
            flash('Esta decoracion ya esta registrado', 'error')
        else:   
            _cost = request.form['costAli']
            _est = request.form['state']
                        
            try:
                p = AdditionalAli( nameAdAli = _name, costAdAli = _cost, idAct = _est )
                
                print(p)
                
                db.session.add(p)
                db.session.commit()

                flash('Registro exitoso', 'success')
                
                return redirect(url_for("events.listar_events"))
            except Exception as e:
                # Manejar cualquier excepción que pueda ocurrir durante la inserción
                flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for("events.listar_events"))


# EDITAR REGISTRO DE ALIMENTO ADICIONAL
@events.route("/e_ad_ali/<id>", methods=["POST"])
@admin_required
def e_ad_ali(id):
    
    _name = request.form["nameAdAli"]
    _cost = request.form["costAdAli"]
    active = request.form['state']
    
    if _name == '' or _cost == '':
        flash('Registro no valido', 'error')
        return redirect(url_for("events.listar_events"))
    else:
        p = app.models.AdditionalAli()
        adAli = p.query.get(id)
        adAli.nameAdAli = _name
        adAli.costAdAli = _cost
        adAli.idAct = active
        
        app.db.session.commit()
        
        return redirect(url_for("events.listar_events"))
    

# BORRAR REGISTRO ALIMENTO ADICIONAL
@events.route("/d_ad_ali/<id>", methods=["POST"])
@admin_required
def d_ad_ali(id):
    p = app.models.AdditionalAli()
    d_ad_ali = p.query.get(id)
    if d_ad_ali:
        app.db.session.delete(d_ad_ali)
        app.db.session.commit()
    else:
        flash('No se ha encontrado el registro a eliminar', 'error')
        
    return redirect(url_for("events.listar_events"))


# CREAR REGISTRO DE OTROS SERVICIOS
@events.route("/c_ots", methods=["POST"])
@admin_required
def agg_ots():
    from app.models import OthersServ
    from app import db
    
    if request.method == 'POST':
    
        _name = request.form['nameOts']
        existing = OthersServ.query.filter_by( nameOtServ = _name ).first()        
        
        if existing:
            flash('Esta servicio ya esta registrado', 'error')
        else:   
            _cost = request.form['costOts']
            _est = request.form['state']
                        
            try:
                p = OthersServ( nameOtServ = _name, costOtServ = _cost, idAct = _est )
                
                print(p)
                
                db.session.add(p)
                db.session.commit()

                flash('Registro exitoso', 'success')
                
                return redirect(url_for("events.listar_events"))
            except Exception as e:
                # Manejar cualquier excepción que pueda ocurrir durante la inserción
                flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for("events.listar_events"))


# EDITAR REGISTRO DE OTROS SERVICIOS
@events.route("/e_ots/<id>", methods=["POST"])
@admin_required
def e_ots(id):
    
    _name = request.form["nameOts"]
    _cost = request.form["costOts"]
    active = request.form['state']
    
    print(_name)
    
    if _name == '' or _cost == '':
        flash('Registro no valido', 'error')
        return redirect(url_for("events.listar_events"))
    else:
        p = app.models.OthersServ()
        ots = p.query.get(id)
        ots.nameOtServ = _name
        ots.costOtServ = _cost
        ots.idAct = active
        
        app.db.session.commit()
        
        return redirect(url_for("events.listar_events"))
    
    

# BORRAR REGISTRO ALIMENTO ADICIONAL
@events.route("/d_ots/<id>", methods=["POST"])
@admin_required
def d_ots(id):
    p = app.models.OthersServ()
    d_ots = p.query.get(id)
    if d_ots:
        app.db.session.delete(d_ots)
        app.db.session.commit()
    else:
        flash('No se ha encontrado el registro a eliminar', 'error')
        
    return redirect(url_for("events.listar_events"))