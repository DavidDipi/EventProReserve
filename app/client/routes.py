from flask import render_template, request, send_from_directory
from . import client_blueprint
import app
import os

@client_blueprint.route('/')
def client_home():
    pagina_actual = request.path
    return render_template('home-client.html', pagina_actual = pagina_actual)

@client_blueprint.route('/my-events')
def my_events():
    pagina_actual = request.path
    return render_template('/pages/my-events.html', pagina_actual = pagina_actual)

@client_blueprint.route('/new-event')
def new_events():
    pagina_actual = request.path
    events = app.models.TypeEvents.query.all()
    return render_template('/pages/new-event.html', pagina_actual = pagina_actual, events = events)