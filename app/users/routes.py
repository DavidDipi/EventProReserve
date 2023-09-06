from flask import render_template, request, flash, redirect, url_for
from . import users_blueprint  # Importa el blueprint localmente
import app  # Importa los modelos necesarios
import bcrypt

@users_blueprint.route("/login", methods=["GET", "POST"])
def login():
    from app import session
    if request.method == 'POST':
        _email = request.form['email']
        _pasword = request.form['password']
        
        # Encuentra el usuario en la base de datos por su correo electrónico
        usuario = app.models.User.query.filter_by(emailUser=_email).first()
        
        if usuario:
            # Verificar contraseña almacenada
            if bcrypt.checkpw(_pasword.encode('utf-8'), usuario.passwordUser.encode('utf-8')):
                session['user_id'] = usuario.idUser
                flash('Inicio exitoso', 'success')
                
                # Verificar rol
                if usuario.rol == 1:
                    return redirect(url_for('admin.admin_home'))
                elif usuario.rol == 2:
                    return redirect(url_for('client.client_home'))
                else:
                    return 'Ocurrio un problema'
            else:
                flash('Contraseña incorrecta', 'danger')
        else:
            flash('Usuario no encontrado', 'danger')
        
    return render_template("/ini/pages/login.html")

@users_blueprint.route("/register", methods=["GET", "POST"])
def new_User():
    from app.models import User, Cliente
    from app import db
    if request.method == 'POST':
        _email = request.form['email']
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
            flash(f'Error: {str(e)}', 'danger')
    return render_template('ini/pages/registro.html')
