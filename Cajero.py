# BASE DE DATOS SIMPLE (Simulando una estructura relacional)
# Cada clave es el número de cuenta y el valor son sus datos
usuarios = {
    "101": {"nombre": "Ana", "pin": "1111", "saldo": 1000},
    "102": {"nombre": "Jhon", "pin": "2222", "saldo": 2000},
    "103": {"nombre": "Brayan", "pin": "3333", "saldo": 3000}
}

print("--- SISTEMA MULTI-USUARIO ---")

# 1. BUSCAR USUARIO


# 2. VALIDACIÓN

        
# 3. TRANSACCIÓN
monto = int(input("¿Cuánto deseas retirar?: $"))
        
    if 0 < monto <= usuario_actual['saldo']:
            usuario_actual['saldo'] -= monto  # Se actualiza solo esa cuenta
            print(f"Retiro exitoso. Nuevo saldo de {usuario_actual['nombre']}: ${usuario_actual['saldo']}")
            print("[LOG]: Operación registrada con éxito.") [cite: 11]
    else:
            print("Error: Saldo insuficiente o monto inválido.")
    else:
            print("Error: PIN incorrecto.")
    else:
            print("Error: La cuenta no existe.")

            print("\nSesión finalizada.")