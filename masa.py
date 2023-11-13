#Autor: wilians Delgadillo C. - Stphanie altamirano
#Fecha:09/11/2023
#Descripcion: Este modulo comvierte los kilos a gramos
def Kilos_gramos(Kilos) :
    return (Kilos * 1000)


if __name__=="__main__":
    
    Kilos= float(input("ingrese los kilos a comvertir \n"))
    print(Kilos_gramos(Kilos))