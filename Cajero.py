# BASE DE DATOS SIMPLE (Simulando una estructura relacional)
# Cada clave es el número de cuenta y el valor son sus datos
usuarios = {
    "101": {"nombre": "Ana", "pin": "1111", "saldo": 1000},
    "102": {"nombre": "Jhon", "pin": "2222", "saldo": 2000},
    "103": {"nombre": "Brayan", "pin": "3333", "saldo": 3000}
}

print("--- SISTEMA MULTI-USUARIO ---")

# 1. BUSCAR USUARIO
cuenta = input("Ingrese su número de cuenta (101, 102, 103): ")

if cuenta in usuarios:
    usuario_actual = usuarios[cuenta]
    pin_ingresado = input(f"Hola {usuario_actual['nombre']}, ingresa tu PIN: ")

# 2. VALIDACIÓN

        
# 3. TRANSACCIÓN
