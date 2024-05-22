import os
import pandas as pd
import datetime

def sesionActivaAdmin():
  """
  Función que mantiene la sesión activa para el administrador.
  Permite al administrador salir del programa o volver al menú principal.
  """
  sesion = input('\n¿Quieres salir? \n (1) Si \n (2) No \n')
  if sesion == '1':
    print('Gracias por usar el programa')
    exit()
  else:
    os.system('cls')
    sesionAdmin()

def sesionActivaVendedor():
  """
  Función que mantiene la sesión activa para el vendedor.
  Permite al vendedor salir del programa o volver al menú principal.
  """
  sesion = input('\n¿Quieres salir? \n (1) Si \n (2) No \n')
  if sesion == '1':
    print('Gracias por usar el programa')
    exit()
  else:
    os.system('cls')
    sesionVendedor()

def sesionAdmin():
  """
  Función que muestra el menú principal y las opciones disponibles para el administrador.
  Permite al administrador seleccionar una opción y realizar las acciones correspondientes.
  """
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
        sesionActivaAdmin()
      case 2:
        print('\n\t\tLitar productos\n')
        listarProductos()
        sesionActivaAdmin()
      case 3:
        print('\n\t\tBuscar producto\n')
        buscarProducto()
        sesionActivaAdmin()
      case 4:
        print('\n\t\tEliminar producto\n')
        eliminarProducto()
        sesionActivaAdmin()
      case 5:
        print('\n\t\tModificar producto\n')
        sesionActivaAdmin()
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

def sesionVendedor():
  """
  Función que muestra el menú principal y las opciones disponibles para el vendedor.
  Permite al vendedor seleccionar una opción y realizar las acciones correspondientes.
  """
  print("\t\tBienvenido a la tienda\n")
  print("\t\tSeleccione una opción:")
  print("\n(1) Listar producto producto"
      "\n(2) Buscar productos"
      "\n(3) Registrar una venta"
      "\n(4) Salir\n"
  )
  try:
    opcion = int(input('Elige una opción: '))
    os.system('cls')
    match opcion:
      case 1:
        print('\n\t\tLitar productos\n')
        listarProductos()
        sesionActivaVendedor()
      case 2:
        print('\n\t\tBuscar producto\n')
        buscarProducto()
        sesionActivaVendedor()
      case 3:
        print('\n\t\tRegistrar una venta\n')
        registrarSalida()
        sesionActivaVendedor()
      case 4:
        print('\n\t\tGracias por usar el programa\n')
        exit()
      case _:
        print('\n\t\tOpción no válida')
        sesionVendedor()
  except ValueError:
    print('Opción no válida')
    os.system('cls')
    sesionVendedor()

def registrarProducto():
  """
  Función que registra un nuevo producto.
  Solicita al usuario ingresar los datos del producto y los guarda en un archivo CSV.
  """
  archivo = open("productos.csv", "a")
  
  try:
    nombreProducto = str(input("Ingrese el nombre del producto: "))
    precioProducto = float(input("Ingrese el precio unitario producto: "))
    cantidadProducto = int(input("Ingrese la cantidad del producto: "))

    precioTotal = precioProducto * cantidadProducto
    fechaActual = datetime.date.today().strftime( "%d/%m/%Y")

    archivo.write(nombreProducto + "," + str(fechaActual) + "," + str(precioProducto) + "," + str(precioTotal) + "," + str(cantidadProducto) + "," + ","+ str(cantidadProducto) + "\n")
    archivo.close()
  except:
    print('Error al ingresar los datos')
    os.system('pause')
    os.system('cls')
    registrarProducto()

def listarProductos():
  """
  Función que lista todos los productos registrados.
  Lee los datos del archivo CSV y muestra la información en forma de tabla.
  """
  df = pd.read_csv('productos.csv')
  print(df.to_string(index=False))

def buscarProducto():
  """
  Función que busca un producto por su nombre.
  Lee los datos del archivo CSV y muestra la información del producto si es encontrado.
  """
  try:
    df = pd.read_csv("productos.csv")
    
    nombreProducto = str(input("Ingrese el nombre del producto a buscar: "))
    
    producto = df.iloc[df.index[df['NOMBRE'] == nombreProducto].tolist()[0], :]
    
    if not producto.empty:
      print(f"{'NOMBRE':<20}{'FECHA':<20}{'PRECIO UNITARIO':<20}{'PRECIO TOTAL':<20}{'ENTRADAS':<20}{'SALIDAS':<20}{'STOCK':<20}")
      print(f"{producto['NOMBRE']:<20}{producto['FECHA']:<20}{producto['PRECIO UNITARIO']:<20}{producto['PRECIO TOTAL']:<20}{producto['ENTRADAS']:<20}{producto['SALIDAS']:<20}{producto['STOCK']:<20}")
    else:
      print("El Producto no fue encontrado")
  except Exception as e:
    print("El Producto no fue encontrado")
    print(f"Error: {e}") 

def eliminarProducto():
  """
  Función que elimina un producto por su nombre.
  Lee los datos del archivo CSV, busca el producto y lo elimina del DataFrame.
  """
  df = pd.read_csv('productos.csv')

  nombreProducto = str(input('Nombre del producto: '))
  try:
    idice = df.index[df['NOMBRE'] == nombreProducto].tolist()[0]
    df.drop([idice], axis=0, inplace=True)
    df.to_csv('productos.csv',index=False)
    print(f'El {nombreProducto} fue eliminado correctamente')
  except Exception as e:
    print('Producto no encontrado')
    print(f'Error: {e}')

def registrarSalida():
  """
  Función que registra una salida de productos.
  Lee los datos del archivo CSV, actualiza la cantidad de salidas y el stock del producto.
  """
  df = pd.read_csv('productos.csv')

  nombreProducto = str(input('Nombre del prodcuto: '))
  cantidadProducto = str(input(f'Numero de {nombreProducto}s a vender: '))

  indice = df.index[df['NOMBRE'] == nombreProducto].tolist()[0]

  entradaProducto = df.iloc[indice,4]
  salidaProducto = df.iloc[indice,5]
  stockActual = df.iloc[indice,6]

  if int(stockActual) < int(cantidadProducto):
    print(f'La cantidad de {nombreProducto}s no es suficente para consilidar la venta\n')
  else:
    stock = int(stockActual) - int(cantidadProducto)
    actualizacionSalida = int(salidaProducto) + int(cantidadProducto)

    df.loc[indice,'SALIDAS'] = actualizacionSalida
    df.loc[indice,'STOCK'] = stock
    df.to_csv('productos.csv',index=False)
    print('Datos actualizados')
    print(df.to_string(index=False))
