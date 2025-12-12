# INICIO CODIGO FUNCIONES #

print("El programa haara una Recolección de Datos de Encuestas de Mercado")

def Leer_Edad():
    edad = int(input("Ingrese la edad del participante (0 para finalizar): "))
    return edad
def Verificar_Rango(edad):
    if edad >= 25 and edad <= 45:
        resultado = "Objetivo"
    else:
        resultado = "No Objetivo"
    return resultado

def Contar_Total(cont_actual):
    nuevo_total = cont_actual + 1
    return nuevo_total
def Contar_Objetivo(cont_actual):
    nuevo_objetivo = cont_actual + 1
    return nuevo_objetivo
def Sumar_Edades(suma_actual, edad):
    nueva_suma = suma_actual + edad
    return nueva_suma

def Unir_Mensaje(mensaje_total, nuevo):
    mensaje_total = mensaje_total + nuevo
    return mensaje_total
def Imprimir_Final(texto):
    print(texto)
    return "Proceso completado."

def Programa():
    total_participantes = 0
    total_objetivo = 0
    suma_edades = 0
    mensajes = ""

    while True:
        edad = Leer_Edad()

        if edad == 0:
            break

        Llamar_Total = Contar_Total(total_participantes)
        total_participantes = Llamar_Total

        Llamar_Verificar = Verificar_Rango(edad)

        if Llamar_Verificar == "Objetivo":
            Llamar_Objetivo = Contar_Objetivo(total_objetivo)
            total_objetivo = Llamar_Objetivo

            nuevo_msg = "Edad registrada (objetivo): " + str(edad) + "\n"
            mensajes = Unir_Mensaje(mensajes, nuevo_msg)

        else:
            nuevo_msg = "Edad registrada (no objetivo): " + str(edad) + "\n"
            mensajes = Unir_Mensaje(mensajes, nuevo_msg)

        Llamar_Suma = Sumar_Edades(suma_edades, edad)
        suma_edades = Llamar_Suma

    if total_participantes > 0:
        promedio = suma_edades / total_participantes
    else:
        promedio = 0

    reporte = "Total participantes: " + str(total_participantes) + "\n"
    reporte = reporte + "Público Objetivo: " + str(total_objetivo) + "\n"
    reporte = reporte + "Promedio de edades: " + str(promedio) + "\n\n"
    reporte = reporte + mensajes
    return reporte

# ZONA FINAL DE CODIGO #
Llamar_Programa = Programa()
Llamar_Imprimir = Imprimir_Final(Llamar_Programa)
print(Llamar_Imprimir)