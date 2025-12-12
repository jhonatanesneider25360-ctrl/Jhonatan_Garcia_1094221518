# Inicio codigo funciones #

print("El programa procesara depósitos y retiros para calcular el saldo final de una cuenta.")

def procesar_transacciones():
    saldo = 50000
    transacciones_validas = 0

    while True:
        tipo = input("Ingrese tipo de transacción (D = Depósito, R = Retiro, FIN = terminar): ").upper()
                                                                                    # .upper() , convierte el texto en str a mayusuclas
        if tipo == "FIN":
            break

        if tipo not in ("D", "R"):
            print(" Tipo de transacción no válido. Intente nuevamente.\n")
            continue

        try:
            monto = float(input("Ingrese el monto: "))
        except:
            print(" Monto inválido.\n")
            continue

        if monto <= 0:
            print(" El monto debe ser mayor que 0.\n")
            continue
        
        if tipo == "D":
            saldo = saldo+monto
            transacciones_validas = transacciones_validas+1
            print(f" Depósito exitoso. Nuevo saldo: {saldo}\n")

        elif tipo == "R":
            if saldo - monto < 0:
                print(" Retiro no permitido. Saldo insuficiente.\n")
            else:
                saldo = saldo-monto
                transacciones_validas = transacciones_validas+1
                print(f" Retiro exitoso. Nuevo saldo: {saldo}\n")

    print(f"Saldo final: {saldo}")
    print(f"Transacciones válidas: {transacciones_validas}")


# Zona De Codigo Final #
Llamar_Transaccion=procesar_transacciones()
print(Llamar_Transaccion)
