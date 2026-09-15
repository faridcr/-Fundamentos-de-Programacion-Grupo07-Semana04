# EJ. 1
# matematicas.py  <- módulo independiente (adaptado para un solo archivo)
def sumar(a, b):      return a + b
def restar(a, b):     return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0: raise ValueError("División por cero")
    return a / b

print("\nEJ.1")
print(sumar(10, 5))    # 15
print(dividir(20, 4))  # 5.0


# EJ. 2
def validar_email(email):
    return "@" in email and "." in email

def validar_password(pwd):
    return len(pwd) >= 8

def validar_formulario(email, pwd):
    return validar_email(email) and validar_password(pwd)

print("\nEJ.2")
print(validar_formulario("a@b.com", "segura123"))  # True


# EJ. 3
def leer_datos(fuente):
    return [1, -2, 3, -4, 5]

def filtrar_positivos(datos):
    return [x for x in datos if x > 0]

def calcular_estadisticas(datos):
    return {
        "suma":  sum(datos),
        "media": sum(datos) / len(datos),
        "max":   max(datos)
    }

print("\nEJ.3")
# Pipeline modular
datos  = leer_datos("archivo.csv")
limpios = filtrar_positivos(datos)
stats  = calcular_estadisticas(limpios)
print(stats)
# {'suma': 9, 'media': 3.0, 'max': 5}
print()