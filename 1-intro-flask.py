from flask import Flask, request

app = Flask(__name__)
productos = [{
    'id': 1,
    'nombre': 'Martillo',
    'precio': 15.8,
    'disponible': True
},
    {
    'id': 2,
    'nombre': 'Serrucho',
    'precio': 20.5,
    'disponible': True
},
    {
    'id': 3,
    'nombre': 'Taladro',
    'precio': 120.0,
    'disponible': False

}]


@app.route('/productos', methods=['GET', 'POST'])
def gestionProductos():
    # request > me da toda la informacion de mi cliente
    if request.method == 'GET':
        return {

            'message': 'los productos son',
            'content': productos

        }
    elif request.method == 'POST':
        print(request.json)
        id = len(productos)+1
        data = request.json
        data["id"] = id
        productos.append(data)

        return {
            'message': 'Producto creado exitosamente'
        }


@app.route('/producto/<int:id>', methods=["GET"])
def gestionProducto(id):
    if request.method == 'GET':
        resultado = None
        for producto in productos:
            if producto['id'] == id:
                resultado = producto
                break
        if resultado == None:
            return {
                'message': 'no se encontro el producto'
            }
        else:
            return {
                'message': 'El producto es'
            }


if __name__ == "__main__":
    app.run(debug=True)
