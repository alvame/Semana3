#Esto  es un comentario
print('Hola a todos')

# Clases en python
class Persona:
    #definit metodo constructor sin argumentos
    def __init__(self, nom, hijos):
        # Atributos
        #crear atributos de una instancia
        self.nombre = nom
        self.hijos = hijos

# Estamos diciendo que juan es de tipo Persona, creamos el objeto juan
juan =  Persona('juan', ['felipe','ana','carlos'])
pass

