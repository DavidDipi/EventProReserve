from flask_login import current_user

def inject_client_name():
    from app.models import Cliente
    if current_user.is_authenticated:
        cliente = Cliente.query.filter_by(idUser=current_user.idUser).first()
        nombre_cliente = cliente.fullnameClient if cliente else None
    else:
        nombre_cliente = None
    return dict(nombre_cliente=nombre_cliente)
