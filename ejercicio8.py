
inventario = [] # global
def agregar(producto):
        global inventario
        inventario.append(producto)
def mostrar():
    for p in inventario:
        print(f" - {p}")

cantidad=int(input("ingrese la cantidad de productos a agregar :"))
for i in range(cantidad):
    producto=input("ingrese un producto :")
    agregar(producto)

print("Inventario:")

mostrar()
    # - Laptop