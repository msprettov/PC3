#PC3 
#Mauro Pretto 
#Manejo de errores  

#2)
lista = input("Ingrese las calificaciones: ")
lista_f =  lista.split(",") 
enteros=[]


for i in lista_f :
    try: 
        calificacion = float(i) 

        enteros.append(calificacion) 
        c=[]
        for n in enteros :
            b = round(n) 
            c.append(b)
        
    
        

    except ValueError: 
        print("Valor incorrecto, intente de nuevo porfavor") 
       
        break
print(f"La lista de calificaciones enteras es: {c}")
