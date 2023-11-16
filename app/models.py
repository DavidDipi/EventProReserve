from app import db
from datetime import datetime

class Est_Active(db.Model):
    __tablename__ = 'est_active'
    idAct = db.Column(db.Integer, primary_key=True)
    estAct = db.Column(db.String(10), nullable=False)

## Modelos
class TypeEvents(db.Model):
    __tablename__ = 'typeeventstbl'
    idTypeEvent = db.Column(db.Integer, primary_key = True)
    nameTypeEvent = db.Column(db.String(30))
    descriptionTypeEvent = db.Column(db.String(60))
    idAct = db.Column(db.Integer, db.ForeignKey('est_active.idAct'))
    
    
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
    
class AmountPeople(db.Model):
    __tablename__ = 'amountPeople'
    idAmountPe = db.Column(db.Integer, primary_key=True)
    AmountPe = db.Column(db.Integer, nullable=False)
    costAmountPe = db.Column(db.Integer, nullable=False)
    idAct = db.Column(db.Integer, db.ForeignKey('est_active.idAct'))

class AdditionalMob(db.Model):
    __tablename__ = 'additionalMob'
    idAdMob = db.Column(db.Integer, primary_key=True)
    nameAdMob = db.Column(db.String(25), nullable=False)
    costAdMob = db.Column(db.Integer, nullable=False)
    idAct = db.Column(db.Integer, db.ForeignKey('est_active.idAct'))

class AdditionalDec(db.Model):
    __tablename__ = 'additionalDec'
    idAdDec = db.Column(db.Integer, primary_key=True)
    nameAdDec = db.Column(db.String(25), nullable=False)
    costAdDec = db.Column(db.Integer, nullable=False)
    idAct = db.Column(db.Integer, db.ForeignKey('est_active.idAct'))


class AdditionalAli(db.Model):
    __tablename__ = 'additionalAli'
    idAdAli = db.Column(db.Integer, primary_key=True)
    nameAdAli = db.Column(db.String(25), nullable=False)
    costAdAli = db.Column(db.Integer, nullable=False)
    idAct = db.Column(db.Integer, db.ForeignKey('est_active.idAct'))

class OthersServ(db.Model):
    __tablename__ = 'othersServ'
    idOtServ = db.Column(db.Integer, primary_key=True)
    nameOtServ = db.Column(db.String(35), nullable=False)
    costOtServ = db.Column(db.Integer, nullable=False)
    idAct = db.Column(db.Integer, db.ForeignKey('est_active.idAct'))
    


"""
class EventsTbl(db.Model):
    __tablename__ = 'eventsTbl'
    idEvent = db.Column(db.Integer, primary_key=True)
    idClient = db.Column(db.Integer, nullable=False)
    idTypeEvent = db.Column(db.Integer, nullable=False)
    idAmountPe = db.Column(db.Integer, nullable=False)
    idAdMob = db.Column(db.Integer, nullable=False)
    idAdDec = db.Column(db.Integer, nullable=False)
    idAdAli = db.Column(db.Integer, nullable=False)
    idOtServ = db.Column(db.Integer, nullable=False)

    client = db.relationship('Cliente', foreign_keys=[idClient])
    type_event = db.relationship('TypeEvents', foreign_keys=[idTypeEvent])
    amount_people = db.relationship('AmountPeople', foreign_keys=[idAmountPe])
    additional_mob = db.relationship('AdditionalMob', foreign_keys=[idAdMob])
    additional_dec = db.relationship('AdditionalDec', foreign_keys=[idAdDec])
    additional_ali = db.relationship('AdditionalAli', foreign_keys=[idAdAli])
    others_serv = db.relationship('OthersServ', foreign_keys=[idOtServ])

"""