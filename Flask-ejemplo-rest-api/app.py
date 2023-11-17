from flask import Flask, jsonify, request
from products import Products

app = Flask(__name__) # este es mi server!

@app.route('/ping')
def ping():
    return jsonify({"Message": "Works!"})

# La lista en JSON a la web <- através de petición GET
@app.route('/products', methods = ['GET'])
def getProducts():
    return jsonify(Products)

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    # instanciar una variable para obtener el producto desde la URL -->'../<string:product_name>'
    # Compresión de listas
    productFound = [product for product in Products if product['nombre'] == product_name]

    if (len(productFound) > 0):
        return  jsonify({"product": productFound[0]})
    return jsonify({"message": " Product Not Found :( "})

@app.route('/products', methods=['POST'])
def addProduct():
    # print(request.json)

    new_product = {
        "name": request.json['nombre'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    # Añadirlo a la lista principal "Products" desde "./products"
    Products.append(new_product)
    # Si lo vamos a añadir a una base de datos deberías iniciar una conexión a ella, hacer un commit de new_product.
    return jsonify({"message": "Nice! Product Added.", "Products": Products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in Products if product['nombre'] == product_name]

    if (len(productFound) > 0):
        productFound[0]['nombre'] = request.json['nombre']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return  jsonify({
            "message": "Product refresh, do it!",
            "Product": productFound[0]
        })
    return jsonify({
        "message": "Uh? not found sorry...",
    })

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFound = [product for product in Products if product['nombre'] == product_name]

    if (len(productFound) > 0):
        Products.remove(productFound[0])
        return jsonify({
            "Which product?": productFound,
            "message": "Done! Your product was deleted..."
        })
    return jsonify({"message": "What u doing, deleted nothingness?"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)