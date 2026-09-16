
def promedio(numeros):
    total = sum(numeros) # local
    n = len(numeros) # local
    return total / n if n else 0

numeros=int(input("ingrese la cantidad de numeros a promediar :"))
lista_numeros=[]
for _ in range(numeros):
    lista_numeros.append(int(input("ingrese un numero :")))
print(promedio(lista_numeros)) # 20.0