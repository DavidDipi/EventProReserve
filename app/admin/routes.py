from flask import render_template, request, send_from_directory, flash, redirect, url_for
from . import admin_blueprint
from flask_login import current_user
import app
import os
import bcrypt

# PAGINA DE INICIO
@admin_blueprint.route('/')
def admin_home():
    if not current_user.is_authenticated or current_user.rol == 2:
        flash('Debe iniciar sesión para acceder a esta página', 'warning')
        return redirect(url_for('users.login'))
    
    
    from app.models import Cliente
    pagina_actual = request.path
    total_clients = Cliente.query.count()
    return render_template('home.html', 
                           pagina_actual = pagina_actual,
                           total_clients = total_clients)
    
    
# LISTA DE USUARIOS   
@admin_blueprint.route('/users')
def admin_users():
    
    if not current_user.is_authenticated or current_user.rol == 2:
        flash('Debe iniciar sesión para acceder a esta página', 'warning')
        return redirect(url_for('users.login'))
    
    ### LISTAR USUARIOS ###
    
    # Obtener página actual    
    pagina_actual = request.path
    
    # Obtener el número de página actual de la solicitud del usuario
    pagina_actual = request.args.get('pag', type=int, default=1)
    
    # Listar usuarios
    registros_por_pagina = 10
    offset = (pagina_actual - 1) * registros_por_pagina
    
    users = app.models.User.query.offset(offset).limit(registros_por_pagina)
    total_users = app.models.User.query.count()
    
    cantidad_paginas = total_users // registros_por_pagina
    if total_users % registros_por_pagina != 0:
        cantidad_paginas += 1
        
    return render_template ("/pages/users.html", 
                            users = users, 
                            pagina_actual = pagina_actual,
                            cantidad_paginas = cantidad_paginas)


# AGREGAR NUEVO ADMINISTRADOR
@admin_blueprint.route("/newadmin", methods = ["POST"])
def new_admin():
    from app.models import User, Admin
    from app import db
    
    if not current_user.is_authenticated or current_user.rol == 2:
        flash('Debe iniciar sesión para acceder a esta página', 'warning')
        return redirect(url_for('users.login'))
    
    if request.method == 'POST':
        _email = request.form['email']
        
        # Verificacion de correo existente
        existing_user = User.query.filter_by( emailUser = _email ).first()
        
        if existing_user:
            flash('El correo electronico ya está registrado.', 'error')
        else:   
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


                # Crear un administrador y agregarlo a la sesión
                admin = Admin(fullnameAdmin=_name, phoneAdmin=_phoneAdmin, idUser=Usua_Id)
                db.session.add(admin)
                db.session.commit()

                flash('Registro exitoso', 'success')
                return redirect(url_for("admin.admin_users"))
            except Exception as e:
                # Manejar cualquier excepción que pueda ocurrir durante la inserción
                flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for("admin.admin_users"))


# DIRECTORIO DE ESTILOS
@admin_blueprint.route('/static/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('static/css', filename)