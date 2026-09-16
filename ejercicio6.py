
MODO_DEBUG = True # global (constante)
def procesar(dato):
    if MODO_DEBUG: # lectura sin 'global'
        print(f"[DEBUG] Procesando: {dato}")
    return dato.upper()

dato=input("Ingrese un dato :")
resultado=procesar(dato)
print(f"Resultado: {resultado}")