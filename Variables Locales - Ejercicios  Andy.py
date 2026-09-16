# ==========================================
# VARIABLES LOCALES - EJERCICIOS EN PYTHON
# ==========================================


# EJERCICIO 1: Contar vocales
def contar_vocales(texto):
    # Guardamos las vocales que vamos a buscar
    vocales = "aeiouAEIOU"

    # Esta variable es local a la función
    # Aquí iremos contando las vocales encontradas
    conteo = 0

    # Recorremos cada letra del texto
    for letra in texto:

        # Comprobamos si la letra pertenece a las vocales
        if letra in vocales:
            conteo += 1

    # Retornamos la cantidad de vocales encontradas
    return conteo


# Probamos la función
print("EJERCICIO 1")
print("Cantidad de vocales:", contar_vocales("Hola Mundo"))
# Resultado: 4


# ==========================================
# EJERCICIO 2: Promedio
# ==========================================

def promedio(numeros):
    # Sumamos todos los números de la lista
    # total es una variable local
    total = sum(numeros)

    # Contamos cuántos números hay
    # n también es una variable local
    n = len(numeros)

    # Calculamos el promedio
    # Si la lista está vacía, retornamos 0
    return total / n if n else 0


# Probamos la función
print("\nEJERCICIO 2")
print("Promedio:", promedio([10, 20, 30]))
# Resultado: 20.0


# ==========================================
# EJERCICIO 3: Celsius a Fahrenheit
# ==========================================

def celsius_a_fahrenheit(c):
    # Factor es una variable local de la función
    factor = 9 / 5

    # Calculamos la temperatura en Fahrenheit
    # fahrenheit también es una variable local
    fahrenheit = c * factor + 32

    # Retornamos el resultado
    return fahrenheit


# Probamos la función con 100 grados Celsius
print("\nEJERCICIO 3")
print("100 °C =", celsius_a_fahrenheit(100), "°F")
# Resultado: 212.0

# Probamos la función con 0 grados Celsius
print("0 °C =", celsius_a_fahrenheit(0), "°F")
# Resultado: 32.0


# ==========================================
# EJERCICIO EXTRA: Variables locales
# ==========================================

def funcion_a():
    # Esta variable es local solamente a funcion_a
    valor = 100

    return valor


def funcion_b():
    # Esta variable también se llama valor,
    # pero es independiente de la variable de funcion_a
    valor = 200

    return valor


# Cada función devuelve su propio valor
print("\nEJERCICIO EXTRA")
print("Valores:", funcion_a(), funcion_b())
# Resultado: 100 200