# ==========================================
# EJERCICIO 1: CUENTA BANCARIA
# Encapsulamiento en Python
# ==========================================


class CuentaBancaria:

    def __init__(self, titular, saldo):
        # El titular es un atributo público
        self.titular = titular

        # Los dos guiones bajos indican que saldo
        # es un atributo privado de la clase
        self.__saldo = saldo

    def depositar(self, monto):
        # Verificamos que el monto sea mayor que cero
        if monto > 0:

            # Aumentamos el saldo
            self.__saldo += monto

    def ver_saldo(self):
        # Retornamos el saldo mediante un método
        # en lugar de acceder directamente al atributo privado
        return self.__saldo


# Creamos una cuenta bancaria
c = CuentaBancaria("Ana", 500)

# Depositamos 200
c.depositar(200)

# Mostramos el saldo actualizado
print("Saldo:", c.ver_saldo())
# Resultado: 700