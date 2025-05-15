from datetime import datetime
from . import db

class Produto(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text,nullable=True)
    codigo_barras = db.Column(db.String(50),unique=True,nullable=False)
    validade = db.Column(db.Date,nullable=True)
    quantidade = db.Column(db.Integer,default=0)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    