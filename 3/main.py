# Ejercicio 2.3 página 66 
from enum import Enum

class carro:
    marca = str
    modelo = int
    motor = int

    class tipoCom(Enum):
        Gasolina = "Gasolina"
        Bioetanol = "Bioetanol"
        Diesel = "Diesel"
        Biodiesel = "Biodiesel"
        Gas_natural = "Gas Natural"

    tipoCombustible = tipoCom

    class tipoA(Enum):
        Ciudad = "Ciudad"
        Subcompacto = "Subcompacto"
        Compacto = "Compacto"
        Familiar = "Familiar"
        Ejecutivo = "Ejecutivo"
        Suv = "Suv"

    tipoAuto = tipoA
    numero_puertas = int
    cantidad_asientos = int
    v_maxima = int

    class tipoColor(Enum):
        Blanco = 1
        Negro = 2
        Rojo = 3
        Naranja = 4
        Amarillo = 5
        Verde = 6
        Azul = 7
        Violeta = 8

    color = tipoColor
    v_actual = int(0)

    def __init__(self, marca: str, modelo: int, motor: int, tipoCombustible: tipoCom, tipoAuto: tipoA, numero_puertas: int,
                 cantidad_asientos: int, v_maxima: int, color: tipoColor, v_actual: int = 0):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipoCombustible = tipoCombustible
        self.tipoAuto = tipoAuto
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.v_maxima = v_maxima
        self.color = color
        self.v_actual = v_actual

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getMotor(self):
        return self.motor

    def getTipoCombustible(self):
        return self.tipoCombustible

    def getTipoAuto(self):
        return self.tipoAuto

    def getNumeroPuertas(self):
        return self.numero_puertas

    def getCantidadAsientos(self):
        return self.cantidad_asientos

    def getVelocidadMaxima(self):
        return self.v_maxima

    def getColor(self):
        return self.color

    def getVelocidadActual(self):
        return self.v_actual

    def setMarca(self, marca: str):
        self.marca = marca

    def setModelo(self, modelo: int):
        self.modelo = modelo

    def setMotor(self, motor: int):
        self.motor = motor

    def setTipoCombustible(self, tipoCombustible):
        self.tipoCombustible = tipoCombustible

    def setTipoAuto(self, tipoAuto):
        self.tipoAuto = tipoAuto

    def setNumeroPuertas(self, numero_puertas):
        self.numero_puertas = numero_puertas

    def setCantidadAsientos(self, cantidad_asientos):
        self.cantidad_asientos = cantidad_asientos

    def setVelocidadMaxima(self, v_maxima):
        self.v_maxima = v_maxima

    def setColor(self, color):
        self.color = color

    def setVelocidadActual(self, v_actual):
        self.v_actual = v_actual

    def acelerar(self, incremento_v: int):
        if (self.v_actual + incremento_v) <= self.v_maxima:
            self.v_actual += incremento_v
        else:
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil")

    def desacelerar(self, decremento_v: int):
        if (self.v_actual - decremento_v) >= 0:
            self.v_actual -= decremento_v
        else:
            print("No se puede decrementar a una velocidad negativa")

    def frenar(self):
        self.v_actual = 0

    def calcular_tiempo_llegada(self, distancia: int):
        if self.v_actual > 0:
            return distancia / self.v_actual
        else:
            print("El vehículo está detenido, no se puede calcular el tiempo de llegada")
            return None

    def imprimir(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Motor: ", self.motor)
        print("Tipo de combustible: ", self.tipoCombustible.value)
        print("Tipo de carro: ", self.tipoAuto.value)
        print("Número de puertas: ", self.numero_puertas)
        print("Cantidad de asientos: ", self.cantidad_asientos)
        print("Velocidad máxima: ", self.v_maxima)
        print("Color: ", self.color.name)


carro1 = carro("Ford", 2018, 3, carro.tipoCom.Diesel, carro.tipoA.Ejecutivo, 5, 6, 250, carro.tipoColor.Negro)
carro1.imprimir()
carro1.setVelocidadActual(100)
print("Velocidad actual: ", carro1.getVelocidadActual())
carro1.acelerar(20)
print("Velocidad actual: ", carro1.getVelocidadActual())
carro1.desacelerar(50)
print("Velocidad actual: ", carro1.getVelocidadActual())
carro1.frenar()
print("Velocidad actual: ", carro1.getVelocidadActual())
carro1.desacelerar(20)