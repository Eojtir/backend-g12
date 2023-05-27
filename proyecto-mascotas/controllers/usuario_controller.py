from flask_restful import Resource,request
from db import conexion
from models.usuarios_model import UsuarioModel
from dtos.usuario_dto import UsuarioResponseDto, UsuarioRequestDto


class UsuariosController(Resource):
    # se define en minuscula siempre, y el self siempre va cuando se define un a clase
    def get(self):
        resultado = conexion.session.query(UsuarioModel).all()
        dto = UsuarioResponseDto(many = True)
        data = dto.dump(resultado)
            
        return {
            'content': data
        }

    def post(self):
        data = request.json
        dto = UsuarioRequestDto()
        data_validate = dto.load(data)
        nvo_usuario = UsuarioModel(**data_validate)
        conexion.session.add(nvo_usuario)
        try:
            conexion.session.commit()

            return {
                'message': 'usuario creado exitosamente'
            },201
        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'Error al crear el usuario',
                'content': error.args
            },400 #bad request es una solicitud por parte del front o del usuario
