# INICIO CODIGO FUNCIONES #

print("Cálculo de Descuentos por Volumen de Ventas")

def Crear_Producto():
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    subtotal = precio * cantidad
    return subtotal
def Acumular_Subtotal(subtotal_actual):
    nuevo_total = subtotal_actual
    return nuevo_total

def Calcular_Descuento(total):
    if total > 1000:
        descuento = "10"
    elif total > 500:
        descuento = "5"
    else:
        descuento = "0"
    return descuento

def Aplicar_Descuento(descuento):
    if descuento == "10":
        mensaje = "Se aplicó un 10% dee descuento."
    elif descuento == "5":
        mensaje = "Se aplicó un 5% de descuento."
    else:
        mensaje = "No se aplicó descuento."
    return mensaje

def Total_Final(total):
    return total

def Imprimir(texto):
    print(texto)
    return "Proceso completado."

def Programa():
    suma_total = 0

    while True:
        opcion = input("¿Deseas ingresar un producto? (SI / STOP): ").upper() 
                                                                    # .upper() , convierte el texto en str a mayusuclas
        if opcion == "STOP":
            break

        subtotal = Crear_Producto()
        acumulado = Acumular_Subtotal(subtotal)
        suma_total += acumulado

    descuento = Calcular_Descuento(suma_total)
    mensaje = Aplicar_Descuento(descuento)

    if descuento == "10":
        suma_total = suma_total - (suma_total * 0.10)
    elif descuento == "5":
        suma_total = suma_total - (suma_total * 0.05)

    total_final = Total_Final(suma_total)

    texto_final = f"Total final a pagar: ${total_final:.2f}\n{mensaje}"
    return texto_final


# ZONA FINAL DE LLAMADOS
Llamar_Programa = Programa()
Llamar_Imprimir = Imprimir(Llamar_Programa)
print(Llamar_Imprimir)
