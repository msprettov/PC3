#PC3 
#Mauro Pretto 
#Manejo de errores 
#1) 
import math

variable =input("La fracción de gasolina restante es: ") 

numeros= variable.split("/") 
numero1 = int(numeros[0])
numero2 = int(numeros[1]) 

fraccion = numero1/numero2 
porcentaje = math.ceil(fraccion*100) 

print(f"La cantidad de combustible restante es {porcentaje} porciento")

#try: 
#   print(numero1/numero2) 
#except: 
   


