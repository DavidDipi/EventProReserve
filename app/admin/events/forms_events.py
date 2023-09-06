from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.file import FileField,FileRequired, FileAllowed
from wtforms.validators import InputRequired,NumberRange, Length

class RegistrarTipoEvento(FlaskForm):
    nameTypeEvent = StringField("Nombre del evento: ",validators=[InputRequired(message="Nombre del evento requerido"),
        Length(max=30, message="Nombre del evento debe tener menos de 30 caracteres")])
    descriptionTypeEvent = StringField("Descripción del evento: ",validators=[InputRequired(message="Descripción del evento requerido"), Length(max=60, message="Nombre del evento debe tener menos de 60 caracteres")])      
    submit = SubmitField("Guardar", render_kw={'class': 'btn-warning'})                                                   