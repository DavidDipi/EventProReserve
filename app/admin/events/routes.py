from flask import render_template, request, jsonify, url_for, redirect
from . import events
import app
from .forms_events import RegistrarTipoEvento
import os

# Rutas del modulo "EVENTOS"

@events.route("/")
def listar_events():
    pagina_actual = request.path
    # Listar eventos
    events = app.models.TypeEvents.query.all()
    return render_template ("/pages/events.html", events = events, pagina_actual = pagina_actual)

@events.route("/new_event", methods=["GET", "POST"])
def new_Event():
    # Definir el formulario
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
    
    return render_template("/pages/newEvent.html", form=form)

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

@events.route("/delete_event/<id>", methods=["POST"])
def delete_event(id):
    p = app.models.TypeEvents()
    event_to_delete = p.query.get(id)  # Load the event from the database
    if event_to_delete:
        app.db.session.delete(event_to_delete)
        app.db.session.commit()
    return redirect(url_for("events.listar_events"))