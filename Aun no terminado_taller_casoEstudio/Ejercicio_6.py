# INICIO CODIGO FUNCIONES #

print("Monitoreo de Uso de CPU del Servidor")

def Leer_CPU():
    lectura = float(input("Ingrese el uso de CPU (%), o un número negativo para finalizar: "))
    return lectura

def Verificar_Critico(uso):
    if uso > 90:
        mensaje = "Alerta: Uso Crítico"
    else:
        mensaje = "Uso Normal"
    return mensaje

def Contar_Medicion(contador_actual):
    nuevo_contador = contador_actual + 1
    return nuevo_contador

def Contar_Criticos(contador_actual):
    nuevo_contador = contador_actual + 1
    return nuevo_contador

def Crear_Reporte(texto):
    return texto

def Imprimir(mensaje):
    print(mensaje)
    return "Proceso completado."

def Programa():
    total_mediciones = 0
    total_criticos = 0
    mensajes = ""

    while True:
        uso_cpu = Leer_CPU()

        if uso_cpu < 0:  
            break

        Llamar_Medicion = Contar_Medicion(total_mediciones)
        total_mediciones = Llamar_Medicion

        Llamar_Verificar = Verificar_Critico(uso_cpu)

        if Llamar_Verificar == "Alerta: Uso Crítico":
            Llamar_Critico = Contar_Criticos(total_criticos)
            total_criticos = Llamar_Critico

        mensajes += f"CPU: {uso_cpu}% -> {Llamar_Verificar}"

    reporte_final = f"Total de mediciones: {total_mediciones}\nTotal de alertas críticas: {total_criticos}\n{mensajes}"
    Llamar_Reporte = Crear_Reporte(reporte_final)
    return Llamar_Reporte


# ZONA CODIGO FINAL #
Llamar_Programa = Programa()
Llamar_Imprimir = Imprimir(Llamar_Programa)
print(Llamar_Imprimir)
