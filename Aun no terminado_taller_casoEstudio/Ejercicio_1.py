# Inicio Codigo_Funciones #

print("El programa analizara la satisfaccion de los clientes con los pedidos segun su puntuacion")

def Crear_Pedido():
    Pedido=int(input("Ingrese la cantidad de pedidos hechos en el mes: "))
    return Pedido

i=0

def Calificar_Pedido(Pedido):
    suma=0
    cont=0
    Cont_Product=1
    for i in range(1,Pedido+1,1) :
        Nombre_Producto=str(input(f"Ingresar producto {Cont_Product}: "))
        Cont_Product=Cont_Product+1
        Valor=float(input("Ingresar el valor del producto: "))
        Calificacion=int(input("Calificacion del 1-5 \n Ingresar calificacion del servicio:  "))
        if Calificacion > 3 and Calificacion <=5:
            print("Gracias por Calificarnos. ")
            cont=cont+1
            suma=suma+Calificacion
        elif Calificacion >=1 and Calificacion <=3:
            print("Gracias por Calificarnos, mejoraremos para un mejor servicio. ")
            cont=cont+1
            suma=suma+Calificacion
        else:
            print("Calificacion Invalida, Calificacion sera ignorada. ")
    return  suma,cont,Cont_Product

def Sacar_Promedio(suma, cont):
    if cont==0:
        return 0
    else:
        Promedio=suma/cont
    return Promedio
    
def imprimir(Promedio):
    print("La valoracion de los servicios al cliente de la empresa es de: ", Promedio)

    
# Zona codigo #
Llamar_creacion=Crear_Pedido()
Llamar_Calificacion=Calificar_Pedido(Llamar_creacion)
suma,cont, Cont_Product= Llamar_Calificacion
Llamar_Promedio=Sacar_Promedio(suma, cont)
Imprimir=imprimir(Llamar_Promedio)
print(Imprimir)