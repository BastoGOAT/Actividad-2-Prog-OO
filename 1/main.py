# 1) ejercicio 2.1 Página 63 definicion de clases
class persona: 
    nombre = ""
    apellidos = ""
    documento_identidad = ""
    año_born = 0
    
    #el Constructor :)
    def __init__(self, nombre:str, apellidos:str, documento_identidad:str, año_born:int): 
        self.nombre= nombre
        self.apellidos = apellidos
        self.documento_identidad= documento_identidad
        self.año_born=año_born

#crear las personas
persona_1 = persona("Alejandro","Restrepo García","1234567890",2007)
persona_2 = persona("Juan","Bueno García","1234567890",2006)

#funcion imprimir
def imprimir(p):
    print("Nombre: ", p.nombre)
    print("Apellidos: ", p.apellidos)
    print("Número de Documento de identidad: ", p.documento_identidad)
    print("Año de nacimiento: ", p.año_born)
    print("---------------")

imprimir(persona_1)
imprimir(persona_2)
