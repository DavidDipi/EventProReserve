from flask_login import current_user

def inject_client_name():
    from app.models import Cliente, Admin
    nombre_cliente = None
    nombre_admin = None
    
    if current_user.is_authenticated:
        cliente = Cliente.query.filter_by(idUser=current_user.idUser).first()
        admin = Admin.query.filter_by(idUser=current_user.idUser).first()
        
        if cliente:
            nombre_cliente = cliente.fullnameClient
        elif admin:
            nombre_admin = admin.fullnameAdmin
        else:
            return "No se ha podido determinar el usuario"
    else:
        nombre_cliente = None
        nombre_admin = None
        
    return dict(nombre_cliente=nombre_cliente, nombre_admin=nombre_admin)
