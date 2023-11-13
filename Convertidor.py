#Autor: wilians Delgadillo C. - Stphanie altamirano
#Fecha:09/11/2023
#Descripcion: Este Modulo es el menu de conversion de unidades

import Temperatura as temp
import masa
import tiempo as tiem



def main():
    while True:
        opcion = input("Bienvenido, que unidades desea convertir?: \n" 
                "0. Salir del programa\n"
                "1. Celsius a Farenheit\n"
                "2. Kilogramos a gramos\n"
                "3. horas a minutos\n"
                "4. Salir del programa\n")
        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                celsius= float(input("Ingrese los grados a convertir \n"))
                print(temp.celsius_fahrenheit(celsius))
            elif opcion == 2:
                gramos= float(input("Ingrese los kilos a comvertir \n"))
                print(masa.Kilos_gramos(gramos))
            elif opcion == 3:
                mins= float(input("ingrese las horas a comvertir \n"))
                print(tiem.horas_mins(mins))     
        except ValueError:
            print("Solo puede ingresar valores numéricos.")

main()