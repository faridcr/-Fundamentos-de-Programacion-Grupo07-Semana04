# EJ. 1
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular   # público
        self.__saldo = saldo     # privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def ver_saldo(self):
        return self.__saldo

print("\nEJ.1")
c = CuentaBancaria("Ana", 500)
c.depositar(200)
print(c.ver_saldo())  # 700


# EJ. 2
class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Bajo cero absoluto")
        self._celsius = valor

print("\nEJ.2")
t = Temperatura()
t.celsius = 25
print(t.celsius)    # 25


# EJ. 3
# Clase Empleado con acceso controlado
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre   = nombre
        self.__salario = salario

    def aumentar_salario(self, pct):
        self.__salario *= (1 + pct / 100)

    @property
    def salario(self):
        return round(self.__salario, 2)

print("\nEJ.3")
e = Empleado("Carlos", 3000)
e.aumentar_salario(10)
print(e.salario)  # 3300.0
print()