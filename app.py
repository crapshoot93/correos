from flask import Flask,redirect,url_for,render_template,request
from flask import jsonify

from clientes import lista_clientes, lista_nombre_clientes
from mailer import send_email

app=Flask(__name__)

@app.route('/')
def entrada():
  return jsonify({"message": "Backend NSolar SPAM DE CORREOS consulta /clientes para ver datos. /clientes/(nombre_del_cliente) o /listaclientes"})

@app.route('/clientes')
def getProducts():
    return jsonify({"clientes" : lista_clientes})
  
@app.route('/clientes/<string:client_name>')
def getCliente(client_name):
  clientsFound = [cliente for cliente in lista_clientes if cliente['NOMBRE'] == client_name]
  if (len(clientsFound) > 0):
    return jsonify({"cliente": clientsFound[0]})
  return jsonify({"message": "Client Not Found!"})

@app.route('/listaclientes')
def getListaNombreClientes():
      return jsonify({"Nombre Clientes" : lista_nombre_clientes})
    
@app.route('/clientes')
def addCliente():
      new_cliente = {
        "NOMBRE" : request.json['NOMBRE'],
        "PARA" : request.json['PARA'],
        "CON_COPIA" : request.json['CON_COPIA'],
        "CON_COPIA_OCULTA" : request.json['CON_COPIA_OCULTA'],
        "ESTIMADO" : request.json['ESTIMADO']
      }
      lista_clientes.append(new_cliente)
      return jsonify({"message": "Cliente Agregado exitosamente", "clientes":lista_clientes})

@app.route('/sendMail', methods=['GET'])
def sendMail():
  print(request.args)
  
  recipientMail = request.args.get('recipientMail')
  send_email(recipientMail)

  return jsonify({"message": "Correo enviado exitosamente"})
  
if __name__ == "__main__":
  app.run(debug=True, port=4000)