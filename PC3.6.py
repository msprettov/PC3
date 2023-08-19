
#PC3 
#Mauro Pretto 
#POO 
#6)

class Punto:
    def __init__(self, X=0, Y=0):
        self.X = X
        self.Y = Y

    def __str__(self):
        return f"({self.X},{self.Y})"

    def cuadrante(self):
        if self.X == 0 and self.Y == 0:
            return "El punto está en el origen"
        elif self.X == 0:
            return "El punto está sobre el eje Y"
        elif self.Y == 0:
            return "El punto está sobre el eje X"
        elif self.X > 0 and self.Y > 0:
            return "El punto está en el primer cuadrante"
        elif self.X < 0 and self.Y > 0:
            return "El punto está en el segundo cuadrante"
        elif self.X < 0 and self.Y < 0:
            return "El punto está en el tercer cuadrante"
        else:
            return "El punto está en el cuarto cuadrante"

    def vector(self, otro_punto):
        return (otro_punto.X - self.X, otro_punto.Y - self.Y)

    def distancia(self, otro_punto):
        distancia = ((otro_punto.X - self.X) ** 2 + (otro_punto.Y - self.Y) ** 2) ** 0.5
        print(f"La distancia entre {self} y {otro_punto} es {distancia}")

class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        return abs(self.punto_final.X - self.punto_inicial.X)

    def altura(self):
        return abs(self.punto_final.Y - self.punto_inicial.Y)

    def area(self):
        return self.base() * self.altura()

