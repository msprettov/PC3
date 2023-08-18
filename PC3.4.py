#PC3 
#Mauro Pretto 
#POO 
# 4) 
class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo 
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

rectangulo = RECTANGULO(int(input("Ingrese el largo: ")),int(input("Ingrese el ancho: ")) )

print("El área del círculo es:", rectangulo.calcular_area()) 




