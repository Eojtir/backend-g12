from flask import Flask,request
from db import db
from models.products_model import ProductsModel
from datetime import datetime


app = Flask(__name__)

#app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:backend@localhost:5432/codigo"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

 

@app.before_request
def first_request():
    db.create_all()

@app.route('/')
def index():
    return("hello word")

@app.route('/products',methods =["GET","POST"])
def products():
    if request.method == "GET":
        return("GET")
    if request.method == "POST":
        json = request.json
        record = ProductsModel(
            name = json['name'],
            stock = json['stock'],
            price = json['price'],
            created_at= datetime(2012, 3, 3, 10, 10, 10), 
            updated_at= datetime(2012, 3, 3, 10, 10, 10), 
            status = json['status']
                )
        db.session.add(record)
        db.session.commit()
        return("Producto guardado con exito!!!")





if __name__ == '__main__':
    app.run(debug=True)
