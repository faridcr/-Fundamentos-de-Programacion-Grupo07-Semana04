
def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    conteo = 0 # local
    for letra in texto:
        if letra in vocales:
            conteo += 1
    return conteo

texto =input("ingrese un texto :")
print(contar_vocales(texto)) # 4