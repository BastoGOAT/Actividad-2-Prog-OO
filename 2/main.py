# 2) ejercicio 2.2 Página 66 Definición de atributos de una clase con tipos primitivos de datos
class planeta:
    nombre = None
    Cantidad_Satelites = 0
    masa = 0
    volumen = 0
    diametro = 0
    distancia_sol = 0
    tipo_planeta = None
    es_Observable = False
    
    def __init__(self, nombre:str,Cantidad_Satelites:int,masa:int,volumen:int,diametro:int,distancia_sol:int,tipo_planeta:str,es_Observable:bool):
        self.nombre = nombre
        self.Cantidad_Satelites = Cantidad_Satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo_planeta = tipo_planeta
        self.es_Observable = es_Observable

def calcular_densidad(masa,volumen):
    densidad = masa/volumen
    return densidad

def esPlanetaExterior(distancia_sol):
    limite = 149597870 * 3.4
    if distancia_sol > limite:
        return True
    else:
        return False
def imprimir(p):
    print("Nombre del planeta: ", p.nombre)
    print("Cantidad de satélites: ", p.Cantidad_Satelites)
    print("Masa del planeta: ", p.masa)
    print("Volumen del planeta: ", p.volumen)
    print("Diametro del planeta: ", p.diametro)
    print("Distancia al sol: ", p.distancia_sol)
    print("Tipo de planeta: ", p.tipo_planeta)
    print("Es observable: ", p.es_Observable)
    print("Densidad del planeta", calcular_densidad(p.masa,p.volumen))
    print("Es planeta exterior", esPlanetaExterior(p.distancia_sol))

Planeta_1 = planeta("Tierra",1,5.9736E24,1.08321E12,12742,150000000,"Terrestre",True)
Planeta_2 = planeta("Júpiter",79,1.899E27,1.4313E15,139820,750000000,"Gaseoso",True)

imprimir(Planeta_1)
imprimir(Planeta_2)

