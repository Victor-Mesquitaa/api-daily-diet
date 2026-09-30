from database import db
from datetime import date 

class Refeicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alimento = db.Column(db.String(80), unique=False, nullable=False)
    descricao = db.Column(db.String(120), unique=False, nullable=False)
    dia = db.Column(db.Date(), unique=False, nullable=False)
    indicador_dieta = db.Column(db.Boolean, default=False, nullable=False)
    