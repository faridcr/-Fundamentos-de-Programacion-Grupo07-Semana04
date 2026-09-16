#Ejercicio 1 
visitas = 0 # global
def registrar_visita():
global visitas
visitas += 1
print(f"Visita #{visitas} registrada")
registrar_visita() # Visita #1
registrar_visita() # Visita #2
print(f"Total: {visitas}") # Total: 2

#Ejercicio 2
MODO_DEBUG = True # global (constante)
def procesar(dato):
if MODO_DEBUG: # lectura sin 'global'
print(f"[DEBUG] Procesando: {dato}")
return dato.upper()
procesar("hola") # [DEBUG] Procesando: hola

#Ejercicio 3
inventario = [] # global
def agregar(producto):
global inventario
inventario.append(producto)
def mostrar():
for p in inventario:
print(f" - {p}")
agregar("Laptop")
agregar("Mouse")
mostrar()
# - Laptop

#Ejercicio 4
# Las listas/dicts se MUTAN sin 'global'
# (porque no se reasigna la referencia)
notas = []
def agregar_nota(n):
notas.append(n) # ← sin 'global'
agregar_nota(95)
print(notas) # [95]

