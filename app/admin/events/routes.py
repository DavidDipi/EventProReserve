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