from flask import render_template, request, flash, redirect, url_for, jsonify
from . import users_blueprint  # Importa el blueprint localmente
import app  # Importa los modelos necesarios
import bcrypt
from flask_login import login_user, login_required, logout_user, current_user, LoginManager


@users_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        _email = request.form['email']
        _password = request.form['password']
        
        # Encuentra el usuario en la base de datos por su correo electrónico
        user = app.models.User.query.filter_by(emailUser=_email).first()
        
        if user and bcrypt.checkpw(_password.encode('utf-8'), user.passwordUser.encode('utf-8')):
            login_user(user)  # Iniciar sesión al usuario
            flash('Inicio exitoso', 'success')
            
            # Redirigir a la página de inicio del usuario o a donde sea necesario
            return redirect(url_for('client.client_home'))
        else:
            flash('Credenciales incorrectas', 'error')
    
    return render_template("/ini/pages/login.html")

@users_blueprint.route('/dashboard')
@login_required  # Asegura que el usuario esté autenticado para acceder a esta vista
def dashboard():
    # Aquí puedes acceder al usuario autenticado a través de current_user
    user_id = current_user.id
    # Ahora puedes usar user_id para buscar en la tabla de Cliente u otras acciones relacionadas con el usuario
    return render_template("dashboard.html")

@users_blueprint.route('/logout')
@login_required  # Asegura que el usuario esté autenticado para cerrar sesión
def logout():
    logout_user()  # Cerrar sesión al usuario
    flash('Sesión cerrada', 'info')
    return redirect(url_for('users.login'))






@users_blueprint.route("/register", methods=["GET", "POST"])
def new_User():
    from app.models import User, Cliente
    from app import db

    if request.method == 'POST':
        _email = request.form['email']
        
        # Verificacion de correo existente
        existing_user = User.query.filter_by( emailUser = _email ).first()        
        
        if existing_user:
            flash('El correo electronico ya está registrado.', 'error')
        else:
            _password = request.form['password']
            _rol = 2
            _name = request.form['fullname']
            _phoneClient = request.form['telefono']
            

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
                cliente = Cliente(fullnameClient=_name, phoneClient=_phoneClient, idUser=Usua_Id)
                db.session.add(cliente)
                db.session.commit()

                flash('Registro exitoso', 'info')
                return redirect(url_for("users.login"))
            except Exception as e:
                # Manejar cualquier excepción que pueda ocurrir durante la inserción
                flash(f'Error: {str(e)}', 'error')
    return render_template('ini/pages/registro.html')