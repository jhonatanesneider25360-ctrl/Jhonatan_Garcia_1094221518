# Inicio codigo funciones #

print("El programa realizará el seguimiento de unidades defectuosas por lote de producción.")

def Crear_Lote():
    Lote = input("Ingrese la cantidad de unidades del lote o escriba STOP para finalizar: ")
    return Lote


def Verificar_Unidades(Lote):
    Lote = int(Lote)
    cont_def = 0
    Mensajes = ""
    contador = 1

    for i in range(1, Lote+1):
        Estado = input(f"Ingresar estado de la unidad {contador} (D=defectuosa / O=OK): ").upper()

        if Estado == "D":
            cont_def += 1
            Mensajes += f"Fallo en unidad {contador}\n"
        elif Estado == "O":
            Mensajes += f"Unidad {contador} OK\n"
        else:
            Mensajes += f"Unidad {contador} estado inválido (ignorado)\n"

        contador += 1

    porcentaje = (cont_def / Lote) * 100
    Mensajes += f"\nPorcentaje de defectuosas: {porcentaje:.2f}%"

    return Mensajes


def Imprimir(Resultado):
    print(Resultado)
    return ""


def Programa():
    while True:
        lote = Crear_Lote()
        if lote.upper() == "STOP":
            return "Proceso finalizado."

        resultado = Verificar_Unidades(lote)
        Imprimir(resultado)


# ZONA DE CÓDIGO FINAL #
Llamar_Programa = Programa()
print(Llamar_Programa)
