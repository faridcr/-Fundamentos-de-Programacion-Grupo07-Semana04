
# Las listas/dicts se MUTAN sin 'global'
# (porque no se reasigna la referencia)
notas = []
def agregar_nota(n):
    notas.append(n) # ← con 'global'

cantidad=int(input("ingrese la cantidad de notas a agregar :"))
for i in range(cantidad):
    nota=int(input("ingrese una nota :"))
    agregar_nota(nota)
print("estas son sus notas : ")
print()
print(notas) # [95]