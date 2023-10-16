from flask import render_template, request, jsonify, flash, redirect, url_for
from . import users
import app
# from .forms_events import RegistrarTipoEvento
import os
import bcrypt

# Rutas del modulo "USUARIOS"

@users.route("/")
def list_users():
    pagina_actual = request.path
    
    # Obtener el número de página actual de la solicitud del usuario
    pagina_actual = request.args.get('pag', type=int, default=1)
    
    # Listar usuarios
    registros_por_pagina = 8
    offset = (pagina_actual - 1) * registros_por_pagina
    
    users = app.models.User.query.offset(offset).limit(registros_por_pagina)
    total_users = app.models.Cliente.query.count()
    
    cantidad_paginas = total_users // registros_por_pagina
    if total_users % registros_por_pagina != 0:
        cantidad_paginas += 1
        
    return render_template ("/pages/users.html", 
                            users = users, 
                            pagina_actual = pagina_actual,
                            cantidad_paginas = cantidad_paginas)

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