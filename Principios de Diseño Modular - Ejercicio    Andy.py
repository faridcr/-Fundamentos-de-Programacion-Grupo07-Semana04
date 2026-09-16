# ==========================================
# EJERCICIO 1: DISEÑO MODULAR
# Archivo: matematicas.py
# ==========================================


# Función para sumar dos números
def sumar(a, b):
    return a + b


# Función para restar dos números
def restar(a, b):
    return a - b


# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b


# Función para dividir dos números
def dividir(a, b):

    # Comprobamos que el divisor no sea cero
    if b == 0:
        raise ValueError("División por cero")

    # Realizamos la división
    return a / b