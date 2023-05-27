from flask_restful import Resource
from db import conexion
from models.usuarios_model import UsuarioModel


class UsuariosController(Resource):
    # se define en minuscula siempre, y el self siempre va cuando se define un a clase
    def get(self):
        resultado = conexion.session.query(UsuarioModel).all()
        print(resultado)

        return {
            'message': 'me hicieron get'
        }

    def post(self):
        nvo_usuario = UsuarioModel(
            nombre='Ritjoe', apellido='Mujica', correo='eojtir@mail.com', dni='17131586')
        conexion.session.add(nvo_usuario)
        try:
            conexion.session.commit()

            return {
                'message': 'usuario creado exitosamente'
            },201
        except Exception as error:
            return {
                'message': 'Error al crear el usuario',
                'content': error.args
            },400 #bad request es una solicitud por parte del front o del usuario
