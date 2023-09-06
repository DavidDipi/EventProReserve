from flask import render_template, request, jsonify, flash, redirect, url_for
from . import users
import app
# from .forms_events import RegistrarTipoEvento
import os
import bcrypt

# Rutas del modulo "USUARIOS"

@users.route("/")
def listar_events():
    pagina_actual = request.path
    # Listar eventos
    users = app.models.User.query.all()
    return render_template ("/pages/users.html", users = users, pagina_actual = pagina_actual)

@users.route("/newadmin", methods = ["GET", "POST"])
def new_admin():
    from app.models import User, Admin
    from app import db
    if request.method == 'POST':
        _email = request.form['email']
        _password = request.form['password']
        _rol = 1
        _name = request.form['fullname']
        _phoneAdmin = request.form['telefono']
        

        usuario = app.models.User()
        try:
            password = _password.encode('utf-8')  # Codificar la contraseña como bytes
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password, salt)
            # Inserta el usuario en la tabla de usuarios
            print(f'ID de usuario registrado: {_email, _password,_rol}')
            usuario = User(emailUser=_email, passwordUser=hashed_password, rol=_rol)
            
            db.session.add(usuario)
            db.session.commit()
            print(f'ID de usuario despues: {usuario.emailUser}')
            

            # Ahora puedes acceder al ID del usuario recién registrado
            Usua_Id = usuario.idUser
            print(f'ID de usuario despues dos: {usuario}')

            # Crear un cliente y agregarlo a la sesión
            admin = Admin(fullnameAdmin=_name, phoneAdmin=_phoneAdmin, idUser=Usua_Id)
            db.session.add(admin)
            db.session.commit()

            flash('Registro exitoso', 'success')
            return redirect(url_for("admin.listar_events"))
        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir durante la inserción
            flash(f'Error: {str(e)}', 'danger')
    return render_template("/pages/newAdmin.html")