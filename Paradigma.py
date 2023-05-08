"""Un programa que pueda sumar. restar, multiplicar y dividir"""
print("Bienvenido, iniciando programa...")
N1 = float(input("Ingrese un numero "))
N2 = float(input("Ingrese otro numero "))
OP = int(input("""Elija una opcion
               1- Suma
               2- Resta
               3- Multiplicar
               4- Dividir"""))
match OP:
    case 1:
        print("Ha elegido suma")
        RES= N1+N2
    case 2:
        print("Ha elegido resta")
        RES=N1-N2
    case 3:
        print("Ha elegido multiplicacion")
        RES=N1*N2
    case other:
        print("Ha elegido division")
        if N2==0:
            RES="La division es invalida"
        else:
            RES=N1/N2
print("El primer numero es", N1, "el segundo es", N2)
print("El resultado es", RES)