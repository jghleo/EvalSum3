import csv
import os
import time
import random
sc_5 = 0
sc_10 = 0
sc_20 = 0
nro = random.randint(1, 1000)
nro += 1
sis = os.system("cls")
Max = [["Nro.Ped", "Cliente", "Dirección", "Sector", "Saco 5kg", "Saco 10kg", "Saco 20kg"]]
dir = []
lizt = []
def menu():
    sis
    time.sleep(0.3)
    l = ("-"*30)
    print(f" {l} \n1. Registrar pedido  \n2. Lista los todos los pedido \n3. Imprimir hoja de ruta \n4. Salir del programa \n{l}")

def ped():
    sis
    l  = ("-"*30)
    Nombre = input("Ingrese el Nombre del cliente: ")
    direccion = input("Ingrese la dirección: ")
    Sector = input("Ingrese el sector/comuna: ")
    while True: 
        try:
            sis
            sc = input(f"{l}\nMenu de selecion de sacos \n1.Saco 5KG \n2.Saco 10KG \n3.Saco 20KG \n4.Salir \n{l} \n")
            if sc == "1":
                sc_5 = int(input("Ingrese la cantidad de sacos: "))
                
            elif sc == "2":
                sc_10 = int(input("Ingrese la cantidad de sacos: "))
            elif sc == "3":
                sc_20 = int(input("Ingrese la cantidad de sacos: "))
            elif sc == "4":
                print("Saliendo del menu")
                break
            else:
                print("Error en selecion \nSOLO marque las casillas disponibles")
                time.sleep(0.3)
        except ValueError:
            print("Error en ingresar la cantidad de sacos, solo puede utilizar numeros enteros")
        lizt.append(nro, Nombre, direccion, Sector, sc_5, sc_10, sc_20)
        max.append(lizt)
        dir.append(direccion)
        for i  in len(Max):
            for elemnt in i:
                return print(elemnt, n=" ")
def lis ():
    sis
    if sc_5 == 0 or sc_10 == 0 or sc_20:
        return print("No hay ningun elemento registrado"), time.sleep(0.4)
    else:
        sis
        return print(f"Saco de 5kg, cantidad : {sc_5} \nSaco de  10kg, cantidad : {sc_10} \nSaco de 20kg, cantidad : {sc_20}"), time.sleep(3)
        

def imp():
    sis
    if dir == None:
        print("No, hay ningun dirrecíon  registrado")
    else:
        with open('texto.txt', 'w', newline=" ") as texto:
            texto.write('Dirreción')
            texto.writerow(dir)
            return print("Se guardo correctamente el archivo")

def salir():
    sis
    with open('archivo.csv', 'w',newline=" ") as archivo:
        archivo.writerow(Max)
        print("Saliendo del programa")
    exit()

while True:
        menu()
        op = input(" Selecione: ")
        if op == "1":
            ped()
        elif op == "2":
            lis()
        elif op == "3":
            imp()
        elif op == "4":
            salir()
        else:
                print("Error en selecion \nSOLO marque las casillas disponibles")