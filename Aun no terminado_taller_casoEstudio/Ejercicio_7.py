# INICIO CODIGO FUNCIONES #

print("Este programa hara una Verificación de Cumplimiento de Metas de Ventas")

def Leer_Ventas():
    ventas = float(input("Ingrese ventas del vendedor (0 o negativo para finalizar): "))
    return ventas
def Verificar_Meta(venta):
    if venta >= 5000:
        resultado = "Meta Cumplida"
    else:
        resultado = "Meta No Cumplida"
    return resultado

def Contar_Vendedores(cont_actual):
    nuevo = cont_actual + 1
    return nuevo
def Contar_Cumplidos(cont_actual):
    nuevo = cont_actual + 1
    return nuevo

def Unir_Mensaje(mensaje_total, nuevo_mensaje):
    mensaje_total = mensaje_total + nuevo_mensaje
    return mensaje_total
def Imprimir_Final(texto):
    print(texto)
    return "Proceso completado."

def Programa():
    total_vendedores = 0
    total_cumplieron = 0
    mensajes = ""

    while True:
        ventas = Leer_Ventas()

        if ventas <= 0:   # finaliza simulación
            break

        Llamar_Contar = Contar_Vendedores(total_vendedores)
        total_vendedores = Llamar_Contar

        Llamar_Verificar = Verificar_Meta(ventas)

        if Llamar_Verificar == "Meta Cumplida":
            Llamar_Cumplidos = Contar_Cumplidos(total_cumplieron)
            total_cumplieron = Llamar_Cumplidos

            nuevo_msg = "Vendedor " + str(total_vendedores) + ": ¡Felicidades! Meta alcanzada.\n"
            mensajes = Unir_Mensaje(mensajes, nuevo_msg)

        else:
            nuevo_msg = "Vendedor " + str(total_vendedores) + ": No alcanzó la meta.\n"
            mensajes = Unir_Mensaje(mensajes, nuevo_msg)

    reporte = "Total vendedores procesados: " + str(total_vendedores) + "\n"
    reporte = reporte + "Vendedores con meta cumplida: " + str(total_cumplieron) + ""
    reporte = reporte + mensajes
    return reporte


# ZONA FINAL DE CODIGO #
Llamar_Programa = Programa()
Llamar_Imprimir = Imprimir_Final(Llamar_Programa)
print(Llamar_Imprimir)
