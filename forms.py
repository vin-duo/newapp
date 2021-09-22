#para os forms 222
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired


    # FORMS

class Criar_ensaio(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    piloto = FloatField('piloto')
    rico = FloatField('rico')
    pobre = FloatField('pobre')
    cp = FloatField('cp')
    pesobrita = FloatField('pesobrita')
    slump = FloatField('slump (mm)')
    umidade = FloatField('umidade (%)')

    submit = SubmitField('Registrar')

class Alfa(FlaskForm):
    alfa = FloatField('Alfa:')
    submit = SubmitField('Registrar')


