
# INICIO CODIGO FUNCIONES #

print("El programa calculara la bonificacion de los empleados segun sus horas extra.")

def Pedir_Horas():
    horas = int(input("Ingrese horas extra (negativo para terminar): "))
    return horas

def Calcular_Bono(horas):
    if horas > 5:
        bono = horas * 15
    else:
        bono = horas * 10
    return bono

def Acumular_Bonos(total, bono):
    total = total + bono
    return total

def Contar_Empleados(contador):
    contador = contador + 1
    return contador

def Mostrar_Final(total_bonos, empleados):
    mensaje = "Total pagado en bonificaciones: " + str(total_bonos) + "\n"
    mensaje = mensaje + "Empleados con bonificacion: " + str(empleados)
    return mensaje

total_bonos = 0
empleados = 0
while True:
    Llamar_Horas = Pedir_Horas()
    if Llamar_Horas < 0:
        break

    Llamar_Bono = Calcular_Bono(Llamar_Horas)
    total_bonos = Acumular_Bonos(total_bonos, Llamar_Bono)
    empleados = Contar_Empleados(empleados)
    print("Bonificacion del empleado:", Llamar_Bono)


# ZONA DE CODIGO FINAL #
LlamaR_Calculo = Calcular_Bono(0)
LlamaR_Acumulado = Acumular_Bonos(total_bonos, 0)
LlamaR_Contador = Contar_Empleados(empleados)
LlamaR_Final = Mostrar_Final(total_bonos, empleados)
print(LlamaR_Final)