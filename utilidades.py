import os
import pandas as pd
import datetime

# <------------------------------------Sesion admin---------------------------------->
def sesionAdmin():
  print("\t\tBienvenido a la tienda\n")
  print("\t\tSeleccione una opción:")
  print("\n(1) Registrar producto"
        "\n(2) Listar productos"
        "\n(3) Buscar producto"
        "\n(4) Eliminar producto"
        "\n(5) Modificar producto"
        "\n(6) Generar reporte"
        "\n(7) Salir\n"
)
  try:
    opcion = int(input('Elige una opción: ')) 
    os.system('cls')
    match opcion:
      case 1:
        print('\n\t\tRegistro de productos\n')
        registrarProducto()
      case 2:
        print('\n\t\tLitar productos\n')
        listarProductos()
      case 3:
        print('\n\t\tBuscar producto\n')
        buscarProducto()
      case 4:
        print('\n\t\tEliminar producto\n')
        #eliminarProducto()
      case 5:
        print('\n\t\tModificar producto\n')
      case 6:
        print('Gracias por usar el programa')
        exit()
      case 7:
        print('')
      case _:
        print('Opción no válida')
        sesionAdmin()
  except ValueError:
    print('Opción no válida')
    os.system('cls')
    sesionAdmin()

# <------------------------------------Sesion vendedor------------------------------->
def sesionVendedor():
  print("\t\tBienvenido a la tienda\n")
  print("\t\tSeleccione una opción:")
  print("\n(1) Registrar producto"
        "\n(2) Listar productos"
        "\n(3) Buscar producto"
        "\n(4) Salir\n"
      )
  try:
    opcion = int(input('Elige una opción: ')) 
    os.system('cls')
    match opcion:
      case 1:
        print('\n\t\tRegistro de productos\n')
        registrarProducto()
      case 2:
        print('\n\t\tLitar productos\n')
        listarProductos()
      case 3:
        print('\n\t\tBuscar producto\n')
        buscarProducto()
      case 4:
        print('\n\t\tEliminar producto\n')
        #eliminarProducto()
      case 5:
        print('\n\t\tModificar producto\n')
      case 6:
        print('Gracias por usar el programa')
        exit()
      case _:
        print('Opción no válida')
        sesionVendedor()
  except ValueError:
    print('Opción no válida')
    os.system('cls')
    sesionVendedor()


# <-----------------------------Registrar un producto-------------------------------->
def registrarProducto():
  # Abrir el archivo en modo escritura
  archivo = open("productos.csv", "a")
  try:
    # Pedir los datos del producto
    nombreProducto = str(input("Ingrese el nombre del producto: "))
    precioProducto = float(input("Ingrese el precio unitario producto: "))
    cantidadProducto = int(input("Ingrese la cantidad del producto: "))

    # Realizar la operación
    precioTotal = precioProducto * cantidadProducto
    fechaActual = datetime.date.today().strftime( "%d/%m/%Y")

    # Escribir los datos en el archivo
    archivo.write(nombreProducto + "," + str(fechaActual) + "," + str(precioProducto) + "," + str(precioTotal) + "," + str(cantidadProducto) + "," + "," + "\n")
    archivo.close()
  except:
    print('Error al ingresar los datos')
    os.system('cls')
    registrarProducto()

# <-------------------------Listar los productos registrados------------------------>
def listarProductos():
  df = pd.read_csv('productos.csv')
  print(df.to_string(index=False))
  

# <-----------------------------Buscar un producto---------------------------------->
def buscarProducto():
  # Abrir el archivo en modo lectura
  archivo = open("productos.csv", "r")
  
  # Pedir el nombre del producto a buscar
  nombreProducto = str(input("Ingrese el nombre del producto a buscar: "))
  
  # Leer el archivo
  for linea in archivo:
    if nombreProducto in linea:
      print('\nNOMBRE   ,FECHA      ,PRECIO UNITARIO ,PRECIO TOTAL ,STOCK')
      print(linea + "\n")
      
  archivo.close()


# <-----------------------------Eliminar un producto-------------------------------->
#def eliminarProducto():
  