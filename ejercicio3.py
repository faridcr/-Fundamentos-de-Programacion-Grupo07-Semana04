
def celsius_a_fahrenheit(c):
    factor = 9 / 5 # local
    fahrenheit = c * factor + 32 # local
    return fahrenheit
c = float(input("ingrese la temperatura en grados celsius :"))
print(celsius_a_fahrenheit(c)) # 212.0
print(celsius_a_fahrenheit(0)) # 32.0