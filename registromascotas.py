import os
nombre_mascotas=[""]*3   #pupy
edad_mascotas=[0]*3  # 3

def insertar():
    for i in range(len(nombre_mascotas)): # .Length en C#
        nombre_mascotas[i]= input(f"Ingrese nombre mascotas: ")
        edad_mascotas[i]=int(input(f"Ingrese edad mascota"))
def mostrar():
    for i in range(len(nombre_mascotas)): # .Length en C#
        print(f"nombre: {nombre_mascotas[i]}, edad: {edad_mascotas[i]}")
def main():
  global nombre_mascotas, edad_mascotas #para modificar las listas declaradas fuera del arreglo
  #arreglos paralelos ambas listas deben tner la misma longitud =3
  nombre_mascotas=[""]*3    ##iniciar la lista vacia para cadenas de longitud 3
  edad_mascotas=[0]*3  ##iniciar la lista vacia pra número enteros de longitud 3 

  opcion=0
  while opcion !=4:    ## opcion distinto a 4 (true)
        os.system('cls' if os.name== 'nt' else 'clear') # limpiar la consola
        print("[1] Insertar mascota (nombre | edad)")
        print("[2] Mostrar mascotas (nombre | edad)")
        print("[3] Eliminar mascotas por nombre (en ambos vectores)")
        print("[4] Salir")
        opcion = int (input("Elija una oppción: "))
        if opcion==1:
            ("insertar")
        elif opcion==2:
            print("mostrar")
        elif opcion==3:
            print("eliminar")
        elif opcion==4:
            print("saliendo...")
        else: print("opcion inválida")
        if opcion !=4: input("Presione para continuar...") # Espere a la interacción del usuario para recargar el menú

main()