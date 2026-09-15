#Ejercicio 1
def generador_id():
    ultimo_id = 0

    def nuevo_id():
        nonlocal ultimo_id
        ultimo_id += 1
        return f"ID-{ultimo_id:04d}"

    return nuevo_id


gen = generador_id()

print(gen())  # ID-0001
print(gen())  # ID-0002



#Ejercicio 2
def crear_acumulador():
    total = 0

    def acumular(valor):
        nonlocal total
        total += valor
        return total

    return acumular


suma = crear_acumulador()

print(suma(10))  # 10
print(suma(5))   # 15



#Ejercicio 3
def crear_interruptor():
    estado = False

    def cambiar():
        nonlocal estado
        estado = not estado
        return "ON" if estado else "OFF"

    return cambiar


switch = crear_interruptor()

print(switch())  # ON
print(switch())  # OFF
print(switch())  # ON