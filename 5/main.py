# 5) ejercicio 2.5 Página 95 Definición de métodos con parámetros

class Cuenta_Bancaria:
    nombre = ""
    apellido = ""
    numero_cuenta= 0
    tipo_cuenta =""
    saldo = 0

    def __init__(self, nombre : str,apellido : str, numero_cuenta : int, tipo_cuenta : str):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta.upper()
        self.saldo = 0

def imprimir(p):
    print("Nombres del titular: ", p.nombre)
    print("Apellidos del titular: ", p.apellido)
    print("Número de cuenta: ", p.numero_cuenta)
    print("Tipo de cuenta", p.tipo_cuenta)
    print("Saldo", p.saldo)

def consultar_saldo(p):
    print("El saldo actual es:", p.saldo)

def consignar(p, valor : int):
    if valor > 0:
        p.saldo = p.saldo + valor
        print(f"Se ha consignado ${valor} en la cuenta. El nuevo saldo es ${p.saldo}")
        return True
    else:
        print("El valor a consignar debe ser mayor que cero")
        return False

def retirar(p, valor : int):
    if (valor > 0) and (valor <= p.saldo):
        p.saldo = p.saldo - valor
        print(f"Se ha retirado $ {valor} en la cuenta.El nuevo saldo es ${p.saldo}")
        return True
    else:
        print("El valor a retirar debe ser menor que el saldo actual.")
        return False

Cuenta_bancaria = Cuenta_Bancaria("Pedro", "Perez", 123456789 , "Ahorros")
imprimir(Cuenta_bancaria)
consignar(Cuenta_bancaria, 200000)
consignar(Cuenta_bancaria, 300000)
retirar(Cuenta_bancaria, 400000)

    
        








