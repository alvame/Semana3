# clase Animal
class Animal:
    # Constructor
    def __init__(self, tipo,color,numpatas):
        self.tipo=tipo
        self.color =color
        self.numpatas = numpatas


        # Funciones
    def Caminar(self):
        pasos = 100
        print('El perro camino un total de', pasos)

    def Comer(self):
        print ('Ya hice mis tres comidas')

boby = Animal('Perro', 'negro','4')
print (boby.Caminar())
print (boby.Comer())
print('soy', boby.tipo, boby.color, 'y tengo' ,boby.numpatas, 'patas')
print('Hola soy un {} y tengo {} patas'.format(boby.tipo, boby.numpatas))

#Clase planta
class Planta:

    def __init__(self, nombre, tamano):
        self.nombre=nombre
        self.tamano=tamano

    def crecer(self):
        print('Soy una planta y estoy creciendo...')

    def respirar(self):
        print('Soy una planta y estoy respirando')

rosa = Planta('Rosa', 'mediano')

print(rosa.respirar())
print(rosa.crecer())
print('Soy una :' ,rosa.nombre, 'y soy de tamano' , rosa.tamano)
