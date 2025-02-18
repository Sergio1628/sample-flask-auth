from database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # id(int), username(str), pass(str)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True) # nullable é uma validação booleana se o valor pode ser nulo ou vazio. Neste contexto, é um valor obrigatório, logo, False
    password = db.Column(db.String(80), nullable=False)