from flask import Flask,redirect,url_for,render_template,request
from flask import jsonify

app=Flask(__name__)

from clientes import lista_clientes

@app.route('/')
def entrada():
  return jsonify({"message": "Backend NSolar SPAM DE CORREOS consulta /clientes para ver datos."})

@app.route('/clientes')
def getClientes():
    return jsonify({"clientes" : lista_clientes})

"""
@app.route('/products/<string:product_name>')
def getProduct(product_name):
  productsFound = [product for product in products if product['name'] == product_name]
  if (len(productsFound) > 0):
    return jsonify({"product": productsFound[0]})
  return jsonify({"message": "Product Not Found!"})

@app.route('/products', methods=['POST'])
def addProduct():
  new_product = {
    "name": request.json['name'],
    "price": request.json['price'],
    "quantity": request.json['quantity']
  }
  products.append(new_product)
  return jsonify({"message":"Product Added Successfully", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
  productFound = [product for product in products if product['name']== product_name]
  if (len(productFound) > 0):
    productFound[0]['name'] = request.json['name']
    productFound[0]['price'] = request.json['price']
    productFound[0]['quantity'] = request.json['quantity']
    return jsonify({
      "message": "Product Updated",
      "product": productFound[0]
    })
  return jsonify({"message": "Product Not Found!"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
  productsFound = [product for product in products if product['name'] == product_name]
  if len(productsFound) > 0:
    products.remove(productsFound[0])
    return jsonify({
      "message": "Product deleted",
      "products": products
    })
  return jsonify({"message": "Product Not found!"})
"""
    
if __name__ == "__main__":
  app.run(debug=True, port=4000)
