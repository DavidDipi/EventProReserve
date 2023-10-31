from app import db
from datetime import datetime

## Modelos
class TypeEvents(db.Model):
    __tablename__ = 'typeeventstbl'
    idTypeEvent = db.Column(db.Integer, primary_key = True)
    nameTypeEvent = db.Column(db.String(30))
    descriptionTypeEvent = db.Column(db.String(60))
    
    
class User(db.Model):
    __tablename__ = 'userstbl'
    idUser = db.Column(db.Integer, primary_key = True)
    emailUser = db.Column(db.String(30))
    passwordUser = db.Column(db.String(255))
    rol = db.Column(db.Integer, db.ForeignKey('rol.idRol'))
    active = db.Column(db.Boolean, default=True)
    
    @property
    def is_active(self):
        return self.active

    def get_id(self):
        return self.idUser

    @property
    def is_authenticated(self):
        return True  # Puedes personalizar esto según tus necesidades

    @property
    def is_anonymous(self):
        return False  # Puedes personalizar esto según tus necesidades    

class Rol(db.Model):
    __tablename__ = 'rol'
    idRol = db.Column(db.Integer, primary_key = True)
    nameRol = db.Column(db.String(15))
    
class Cliente(db.Model):
    __tablename__ = 'clientsTbl'
    idCliente = db.Column(db.Integer, primary_key = True)
    fullnameClient = db.Column(db.String(60))
    phoneClient = db.Column(db.String(11))
    idUser = db.Column(db.Integer, db.ForeignKey('userstbl.idUser'))
    
class Admin(db.Model):
    __tablename__ = 'adminTbl'
    idAdmin = db.Column(db.Integer, primary_key = True)
    fullnameAdmin = db.Column(db.String(60))
    phoneAdmin = db.Column(db.String(11))
    idUser = db.Column(db.Integer, db.ForeignKey('userstbl.idUser'))
