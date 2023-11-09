from flask import render_template, request, flash, redirect, url_for, jsonify
from . import users_blueprint  # Importa el blueprint localmente
from functools import wraps
import app  # Importa los modelos necesarios
import bcrypt
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
# from app.context_processors import inject_client_name


def redirect_if_authenticated(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            if current_user.rol == 1:
                return redirect(url_for('admin.admin_home'))
            elif current_user.rol == 2:
                return redirect(url_for('client.client_home'))
            # Añade más condiciones para otros roles si es necesario
        return func(*args, **kwargs)
    return decorated_function


@users_blueprint.route("/login", methods=["GET", "POST"])
@redirect_if_authenticated
def login():
    
    if request.method == 'POST':
        _email = request.form['email']
        _password = request.form['password']
        
        # Encuentra el usuario en la base de datos por su correo electrónico
        user = app.models.User.query.filter_by(emailUser=_email).first()
        
        if user and bcrypt.checkpw(_password.encode('utf-8'), user.passwordUser.encode('utf-8')):
            
            
            login_user(user)  # Iniciar sesión al usuario
            flash('Inicio exitoso', 'success')
            
            # Redirigir a la página de inicio del usuario según su rol
            if user.rol == 1:
                return redirect(url_for('admin.admin_home'))
            elif user.rol == 2:
                return redirect(url_for('client.client_home'))
            # Añade más condiciones para otros roles si es necesario
            
            flash('Rol de usuario no válido', 'error')
            
            # Redirigir a la página de inicio del usuario o a donde sea necesario
            return render_template("/ini/pages/login.html")
        else:
            flash('Credenciales incorrectas', 'error')
            
            
    
    return render_template("/ini/pages/login.html")


@users_blueprint.route('/logout')
@login_required  # Asegura que el usuario esté autenticado para cerrar sesión
def logout():
    logout_user()  # Cerrar sesión al usuario
    flash('Sesión cerrada', 'info')
    return redirect(url_for('users.login'))


@users_blueprint.route("/register", methods=["GET", "POST"])
@redirect_if_authenticated
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

                flash('Registro exitoso', 'success')
                return redirect(url_for("users.login"))
            except Exception as e:
                # Manejar cualquier excepción que pueda ocurrir durante la inserción
                flash(f'Error: {str(e)}', 'error')
    return render_template('ini/pages/registro.html')