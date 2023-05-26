from sqlalchemy.schema import Column,ForeignKey
from sqlalchemy import types
from db import conexion
from enum import Enum

class SexoEnum(Enum):
    Macho = 'Macho'
    Hembra = 'Hembra'
    Otro = 'Otro'


class MascotasModel(conexion.Model):
    id = Column(autoincrement = True,type_=types.Integer,primary_key=True)
    nombre = Column(type_=types.Text,nullable=False)
    apellido = Column(type_=types.Text,nullable=True)
    sexo = Column(type_=types.Enum(SexoEnum),nullable=False)
    fechaNacimiento = Column(type_=types.Date,nullable=False,name='fecha_nacimiento')
    raza = Column(type_=types.Text,default='otro')
    usuarioId = Column( ForeignKey(column='usuarios.id'), type_ = types.Integer,nullable=False,name = 'usuario_id')

    __tablename__ = 'mascotas'

