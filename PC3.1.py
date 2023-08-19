#PC3 
#Mauro Pretto 
#Manejo de errores 
#1) 

import math

while True:
    try:
        fraccion = input("Introduce una fracción en formato X/Y: ")
        x, y = map(int, fraccion.split("/"))
        porcentaje = x / y * 100 
      
        break
     

    except ValueError:
        print("Error: la fracción debe estar en formato X/Y, donde X e Y son números enteros")
    
    
    except ZeroDivisionError:
        print("Error: el denominador no puede ser cero.")

 
if porcentaje < 1:
    print("E")
elif porcentaje > 99:
    print("F")
else:
    print(math.ceil(porcentaje), "%") 

    


   


