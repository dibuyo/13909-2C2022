#Ejercicio A
#Realizar un programa que  determine si el polígono ingresado es un triángulo en 
#base a los grados de sus tres ángulos internos. 
#Si la suma de los tres ángulos es igual a  180º es un triángulo, 
#de lo contrario mostrar que no lo es. De tratarse de un triángulo,
#verifique si alguno de sus ángulos es recto (90º), 
#de cumplirse mostrar que se trata de un triángulo rectángulo. 
#De no ser si no mostrar nada.

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
    