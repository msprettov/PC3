#PC3 
#Mauro Pretto 
#POO 
#3) 

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)

circulo = CIRCULO(int(input("Ingrese el radio: ")))
print("El área del círculo es:", circulo.calcular_area()) 


