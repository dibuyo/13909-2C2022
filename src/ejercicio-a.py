#Ejercicio A
print("Clase 9 - Ejercicio A")
print("Actividad obligatoria - Martín Rivas")

lados = int(input("Ingrese la cantidad de lados del poligono: "))
vertice = 0
sumAngulos = 0
rectangulo = 0

if lados != 3:
    print("No es un rectangulo")
else:
    for vertice in range(0,3):
        angulo = int(input("Ingrese el angulo del vertice #" + str(vertice+1) + ": "))
        if angulo == 90:
            rectangulo += 1
        sumAngulos += angulo
    if sumAngulos <= 180:
        if rectangulo >= 1:
            print("Triangulo con " + str(rectangulo)+ " angulo/s rectos.")
        else:
            if sumAngulos % 3 == 0:
                print("Es un triangulo equilatero.")
            else:
                print("Es un triangulo sin algunos de 90º.")
    