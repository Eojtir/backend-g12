from flask import Flask
from db import conexion
from flask_restful import Api
from flask_migrate import Migrate
from models.usuarios_model import UsuarioModel
from models.mascotas_model import MascotasModel
from controllers.usuario_controller import UsuariosController


app = Flask(__name__)

api = Api(app=app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:password@localhost:5432/mascotas'
conexion.init_app(app)

Migrate(app, conexion)

api.add_resource(UsuariosController,'/usuarios','/otra_ruta')#ambos aputan al mismo controlador

if __name__ == '__main__':

    app.run(debug=True)
