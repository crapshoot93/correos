import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="162.241.60.240",
  user="zentogot_nsolar",
  password="Nsolar2021",
  database="zentogot_crm_nsolar"
)

def getClientes():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Clientes")

    Clientes =  mycursor.fetchall()

    lista_clientes = pd.DataFrame(Clientes)
    lista_clientes.columns = ['ID_CLIENTE', 'NOMBRE', 'PARA', 'CON_COPIA', 'CON_COPIA_OCULTA', 'ESTIMADO', 'CANTIDAD_SISTEMAS']
    del(lista_clientes['CANTIDAD_SISTEMAS'])
    dict_clientes = lista_clientes.to_dict('records')
    return dict_clientes

lista_clientes = getClientes()

def getNombreClientes():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Clientes")

    Clientes =  mycursor.fetchall()

    lista_clientes = pd.DataFrame(Clientes)
    lista_clientes.columns = ['ID_CLIENTE', 'NOMBRE', 'PARA', 'CON_COPIA', 'CON_COPIA_OCULTA', 'ESTIMADO', 'CANTIDAD_SISTEMAS']
    del(lista_clientes['CANTIDAD_SISTEMAS'])
    lista_nombre_clientes = []
    lista_nombre_clientes = lista_clientes['NOMBRE']
    return lista_nombre_clientes
  
lista_nombre_clientes = list(getNombreClientes())
      


