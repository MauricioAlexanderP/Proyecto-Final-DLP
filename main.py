from utilidades import *


# Función principal
def main():
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
  
if __name__ == "__main__":
  main()