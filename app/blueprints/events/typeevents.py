# Modulos
from flask import render_template, request, redirect, send_from_directory, current_app

# from flask_sqlalchemy import SQLAlchemy
from flask import send_from_directory
import os
from flaskext.mysql import MySQL

from blueprints.admin import admin_blueprint
# from models.typeEvent import TipoEvento



@admin_blueprint.route('/events')
def admin_events():
    pagina_actual = request.path 
    
    """
    sql = "SELECT * FROM typeeventstbl;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    clientes = cursor.fetchall()
    conn.commit()"""
    
    tipos_evento = TipoEvento.query.all()
    return render_template('admin/pages/events.html', pagina_actual = pagina_actual, tipos_evento = tipos_evento)