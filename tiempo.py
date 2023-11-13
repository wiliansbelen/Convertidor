#Autor: wilians Delgadillo C. - Stphanie altamirano
#Fecha:09/11/2023
#Descripcion: Este modulo comvierte las horas a minutos

def horas_mins(minutos) :
    return (minutos* 60)

if __name__=="__main__" :
    minutos = float(input("Ingrese los minutos a comvertir \n"))
    print(horas_mins(minutos))