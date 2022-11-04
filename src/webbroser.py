import webbrowser
import time

print ("Visitando Universidades.........")
time.sleep(3)
print ("Menu de opciones")
print ("1-UNLa")
print ("2-UnDav")
print ("3-UNQ")

continua="S"
while continua=="S":
    
    opcion=int(input("Ingrese opción: "))
    if opcion==1:
        webbrowser.open('http://www.unla.edu.ar')
        
    elif opcion==2:
        webbrowser.open('http://www.undav.edu.ar')
   
    else:
        webbrowser.open('http://www.unq.edu.ar')
   
    continua=input("Sigue...?")