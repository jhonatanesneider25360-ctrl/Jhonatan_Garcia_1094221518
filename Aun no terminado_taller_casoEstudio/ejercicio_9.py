# INICIO CODIGO FUNCIONES #
 
print("Control de Inventario con Reposición")

def Stock_Inicial():
    stock = 50
    return stock
def Leer_Venta():
    venta = int(input("Ingrese cantidad vendida del día: "))
    return venta

def Restar_Stock(stock_actual, venta):
    nuevo_stock = stock_actual - venta
    return nuevo_stock

def Verificar_Reposicion(stock):
    if stock <= 10:
        mensaje = "Aviso de Reposición Urgente"
    else:
        mensaje = "Stock Suficiente"
    return mensaje

def Unir_Mensaje(total, nuevo):
    total = total + nuevo
    return total
def Imprimir_Final(texto):
    print(texto)
    return "Proceso completado."

def Programa():
    stock_actual = Stock_Inicial()
    mensajes = ""
    ventas_totales = 0

    while True:
        Llamar_Venta = Leer_Venta()

        Llamar_Restar = Restar_Stock(stock_actual, Llamar_Venta)
        stock_actual = Llamar_Restar

        ventas_totales = ventas_totales + Llamar_Venta

        Llamar_Verificar = Verificar_Reposicion(stock_actual)

        if Llamar_Verificar == "Aviso de Reposición Urgente":
            nuevo_mensaje = "Stock actual: " + str(stock_actual) + " -> Aviso de Reposición Urgente\n"
            mensajes = Unir_Mensaje(mensajes, nuevo_mensaje)
            break
        else:
            nuevo_mensaje = "Stock actual: " + str(stock_actual) + " -> Stock Suficiente\n"
            mensajes = Unir_Mensaje(mensajes, nuevo_mensaje)

    reporte = "Ventas Totales: " + str(ventas_totales) + "\n"
    reporte = reporte + "Stock Final: " + str(stock_actual) + "\n\n"
    reporte = reporte + mensajes
    return reporte

# ZONA CODIGO FINAL #
Llamar_Programa = Programa()
Llamar_Imprimir = Imprimir_Final(Llamar_Programa)
print(Llamar_Imprimir)