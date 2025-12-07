# Inicio Codigo_Funciones #

codigo_acceso = "INV-001"  
accesos_denegados = 0

print("=== Sistema de Control de Acceso ===")
print("Ingrese 'SALIR' para terminar.\n")

while True:
    codigo_ingresado = input("Ingrese el código de identificación: ")

    # Condición de salida
    if codigo_ingresado.upper() == "SALIR":
        break

    # Verificación de credenciales
    if codigo_ingresado == codigo_acceso:
        accesos_permitidos += 1
        print("✔ Acceso exitoso. Bienvenido al área de almacén.\n")
    else:
        accesos_denegados += 1
        print("✖ Acceso denegado. Código incorrecto.\n")

# zona codigo #
print("\n Resumen del Sistema..  ")
print("Accesos permitidos:", accesos_permitidos)
print("Accesos denegados:", accesos_denegados)
print("Sistema finalizado.")