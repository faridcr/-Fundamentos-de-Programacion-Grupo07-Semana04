# ==========================================
# VARIABLES NO LOCALES (NONLOCAL)
# ==========================================


# ==========================================
# EJERCICIO 1: Generador de ID
# ==========================================

def generador_id():

    # Esta variable pertenece a la función generador_id
    # y será utilizada por la función interna nuevo_id.
    ultimo_id = 0

    def nuevo_id():

        # Indicamos que queremos modificar la variable
        # ultimo_id que pertenece a la función externa.
        nonlocal ultimo_id

        # Aumentamos el número de ID
        ultimo_id += 1

        # Retornamos el ID con formato
        return f"ID-{ultimo_id:04d}"

    # Retornamos la función interna
    return nuevo_id


# Creamos un generador de IDs
gen = generador_id()

# Cada llamada aumenta el número anterior
print(gen())  # ID-0001
print(gen())  # ID-0002


# ==========================================
# EJERCICIO 2: Acumulador
# ==========================================

def crear_acumulador():

    # Esta variable pertenece a crear_acumulador
    total = 0

    def acumular(valor):

        # Usamos nonlocal para modificar
        # la variable total de la función externa.
        nonlocal total

        # Sumamos el valor al total
        total += valor

        # Mostramos el total actual
        return total

    # Retornamos la función acumular
    return acumular


# Creamos un acumulador
suma = crear_acumulador()

# Cada llamada conserva el valor anterior
print(suma(10))  # 10
print(suma(5))   # 15


# ==========================================
# EJERCICIO 3: Interruptor
# ==========================================

def crear_interruptor():

    # Variable perteneciente a la función externa
    estado = False

    # Función interna que cambia el estado
    def cambiar():

        # Indicamos que vamos a modificar
        # la variable estado de la función externa.
        nonlocal estado

        # Cambiamos True por False o False por True
        estado = not estado

        # Si estado es True mostramos ON,
        # de lo contrario mostramos OFF.
        return "ON" if estado else "OFF"

    # Retornamos la función cambiar
    return cambiar


# Creamos nuestro interruptor
switch = crear_interruptor()

# Cada llamada cambia el estado
print(switch())  # ON
print(switch())  # OFF
print(switch())  # ON