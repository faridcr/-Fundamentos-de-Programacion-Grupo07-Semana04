#Ejercicio 1
def contar_vocales(texto):
vocales = "aeiouAEIOU"
conteo = 0 # local
for letra in texto:
if letra in vocales:
conteo += 1
return conteo
print(contar_vocales("Hola Mundo")) # 4

#Ejercicio 2
def promedio(numeros):
total = sum(numeros) # local
n = len(numeros) # local
return total / n if n else 0
print(promedio([10, 20, 30])) # 20.0

#Ejercicio 3
def celsius_a_fahrenheit(c):
factor = 9 / 5 # local
fahrenheit = c * factor + 32 # local
return fahrenheit
print(celsius_a_fahrenheit(100)) # 212.0
print(celsius_a_fahrenheit(0)) # 32.0

#Ejercicio 4
def funcion_a():
valor = 100 # local a funcion_a
return valor
def funcion_b():
valor = 200 # local a funcion_b (independiente)
return valor
print(funcion_a(), funcion_b()) # 100 200
