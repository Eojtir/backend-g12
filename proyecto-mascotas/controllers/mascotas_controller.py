from flask_restful import Resource,request
from db import conexion
from models.mascotas_model import MascotasModel
from dtos.mascota_dto import MascotaRequestDto


class MascotasController(Resource):
    def post(self):
        data = request.json
        try:
            dto = MascotaRequestDto()
            dataValidada = dto.load(data)
            nuevaMascota = MascotasModel(**dataValidada)
            conexion.session.add(nuevaMascota)
            conexion.session.commit()
            return{
                'message':'Mascota creada con exito'
            },201

        except Exception as error:
            conexion.session.rollback()

            return{
            'message':'Error al crear la mascota',
            'content' :error.args
            
        },201
    
    def get(self):
        return{

        }