# 4) ejercicio 2.4 Página 86 Definición de métodos con y sin valores de retorno

class circulo:
    radio = 0
    
    def __init__(self, radio:int):
        self.radio = radio
    
    def area(self):
        return (self.radio ** 2) * 3.1416
    
    def perimetro(self):
        return self.radio*2*3.1416

class rectangulo:
    base = 0
    altura = 0
    
    def __init__(self, base:int, altura:int):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (2* self.base) + (2* self.altura)

class cuadrado:
    lado = 0

    def __init__(self, lado:int):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return self.lado * 4

class triangulo_rectangulo:
    base = 0
    altura = 0

    def __init__(self, base:int, altura:int):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura)/2
    
    def perimetro(self):
        return self.base + self.altura + self.hipotenusa()
    
    def hipotenusa(self):
        return ((self.base ** 2) + (self.altura ** 2))**(1/2)
    
    def tipo_triangulo(self):
        if (self.base == self.altura) and (self.base == self.hipotenusa()) and (self.altura == self.hipotenusa()):
            print("Es un triangulo equilátero")
        
        elif (self.base != self.altura) and (self.base != self.hipotenusa()) and (self.altura != self.hipotenusa()):
            print("Es un triangulo escaleno")
        
        else:
            print("Es un triangulo isóceles")
    
class Prueba_figuras:
    def __init__(self):
        figura1= circulo(2)
        figura2= rectangulo(1,2)
        figura3= cuadrado(3)
        figura4= triangulo_rectangulo(3,5)

        print("El área del círculo es = ",figura1.area())
        print("El perímetro del círculo es = ", figura1.perimetro())
        print()
        
        print("El área del rectángulo es = ", figura2.area())
        print("El perímetro del rectángulo es = ", figura2.perimetro())
        print()
        
        print("El área del cuadrado es = ", figura3.area())
        print("El perímetro del cuadrado es = ", figura3.perimetro())
        print()
        
        print("El área del triángulo es = ", figura4.area())
        print("El perímetro del triángulo es = ", figura4.perimetro())
        figura4.tipo_triangulo()

Prueba_figuras()
        












        