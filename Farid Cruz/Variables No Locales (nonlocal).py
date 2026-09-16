# EJ. 1
def generador_id():
    ultimo_id = 0

    def nuevo_id():
        nonlocal ultimo_id
        ultimo_id += 1
        return f"ID-{ultimo_id:04d}"

    return nuevo_id

print("\nEJ.1")
gen = generador_id()
print(gen())  # ID-0001
print(gen())  # ID-0002


# EJ. 2
def crear_acumulador():
    total = 0
    def acumular(valor):
        nonlocal total
        total += valor
        return total
    return acumular

print("\nEJ.2")
suma = crear_acumulador()
print(suma(10))  # 10
print(suma(5))   # 15


# EJ. 3
def crear_interruptor():
    estado = False

    def cambiar():
        nonlocal estado
        estado = not estado
        return "ON" if estado else "OFF"

    return cambiar

print("\nEJ.3")
switch = crear_interruptor()
print(switch())  # ON
print(switch())  # OFF
print(switch())  # ON
print()