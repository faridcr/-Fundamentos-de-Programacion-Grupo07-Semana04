# ==========================================
# VARIABLES GLOBALES - EJERCICIOS EN PYTHON
# ==========================================


# ==========================================
# EJERCICIO 1: Variable global
# ==========================================

# Esta variable se encuentra fuera de las funciones,
# por eso es una variable global.
visitas = 0


def registrar_visita():
    # Indicamos que vamos a utilizar la variable
    # global "visitas" dentro de esta función.
    global visitas

    # Aumentamos en 1 la cantidad de visitas
    visitas += 1

    # Mostramos la cantidad de visitas registradas
    print(f"Visita #{visitas} registrada")


# Registramos dos visitas
registrar_visita()  # Visita #1
registrar_visita()  # Visita #2

# Mostramos el total de visitas
print("Total de visitas:", visitas)
# Resultado: 2


# ==========================================
# EJERCICIO 2: Variable global constante
# ==========================================

# Esta variable se encuentra fuera de la función,
# por eso es una variable global.
# Se utiliza como una constante del programa.
MODO_DEBUG = True


def procesar(dato):
    # Podemos leer MODO_DEBUG dentro de la función
    # sin utilizar la palabra "global".
    if MODO_DEBUG:

        # Mostramos un mensaje de depuración
        print(f"[DEBUG] Procesando: {dato}")

    # Retornamos el dato recibido
    return dato.upper()


# Llamamos a la función
procesar("hola")
# Resultado: [DEBUG] Procesando: hola


# ==========================================
# EJERCICIO 3: Lista global
# ==========================================

# Creamos una lista global para almacenar productos.
inventario = []


def agregar(producto):
    # Como solamente modificamos el contenido de la lista
    # utilizando append(), no es necesario escribir "global".
    inventario.append(producto)


def mostrar():
    # Recorremos los elementos de la lista global.
    for p in inventario:

        # Mostramos cada producto
        print(f"- {p}")


# Agregamos productos al inventario
agregar("Laptop")
agregar("Mouse")

# Mostramos los productos registrados
mostrar()

# Resultado:
# - Laptop
# - Mouse


# ==========================================
# EJERCICIO 4: Modificar una lista global
# ==========================================

# Creamos una lista global de notas.
notas = []


def agregar_nota(n):
    # Agregamos una nota a la lista global.
    # No necesitamos "global" porque no estamos
    # reemplazando la lista, solamente modificando su contenido.
    notas.append(n)


# Agregamos una nota
agregar_nota(95)

# Mostramos la lista de notas
print(notas)
# Resultado: [95]