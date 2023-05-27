from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.mascotas_model import MascotasModel


class MascotaRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = MascotasModel
        include_fk = True  #valida las claves foraneas