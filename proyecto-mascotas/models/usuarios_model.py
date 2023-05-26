from sqlalchemy.schema import Column
from sqlalchemy import types
from db import conexion

#style calmecase con la oprimera mayuscula asi se crean las clases
class UsuarioModel(conexion.Model):
    id = Column(type_ = types.Integer,autoincrement=True,primary_key=True)
    nombre =Column(type_ = types.String(100),nullable=False)
    apellido = Column(type_ = types.String(100),nullable=True)
    correo = Column(type_=types.String(200),nullable=False,unique=True)
    dni = Column(type_ = types.String(14),nullable=False,unique=True)
    __tablename__ = 'usuarios'
