from utilidades import *


# Función principal
def main():
  """
  Esta función es el punto de entrada del programa.
  Solicita al usuario que inicie sesión y redirige a la sesión correspondiente según las credenciales proporcionadas.
  """
  print("\t\tBienvenido a la tienda\n")
  print("\t\tPor favor inicie sesión\n")
  
  usuario = input("Usuario: ")
  contrasena = input("\nContraseña: ")

  if usuario == "admin" and contrasena == "1234":
    print("\nSesión iniciada correctamente\n")
    sesionAdmin()
  elif usuario == "vendedor" and contrasena == "5678":
    print("\nSesión iniciada correctamente\n")
    sesionVendedor()
  else:
    print('Nombre de usuario o contraseña incorrectos')
    main()
if __name__ == "__main__":
  main()