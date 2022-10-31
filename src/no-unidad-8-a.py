#Ejercicio A - Unidad 8
#Martín Rivas

#Se intenta preparar budines de pan. Los ingredientes para 4 personas de la receta son los indicados en el cuadro adjunto. 
#Realizar un algoritmo que calcule los ingredientes para un número variable de personas que se lee por teclado.

print("Clase 8 - Ejercicio A")
print("Actividad No Obligatoria - Martín Rivas")

pan = 2 #unidad
huevos = 3 #unidad
azucar = 0.5 #kg
agua = 1 #taza
porcion = 4

comensales = 0
comensales = int(input("Ingrese la cantidad de personas para calcular la receta de budines: "))

factor = comensales/porcion
print("Debe cocinar " + str(factor) + " budines.")

print("Vas a necesitar: ")
print(pan*factor, " pan/es con cáscara")
print(huevos*factor, " huevo/s batidos")
print(azucar*factor, " kilo/s de azúcar")
print(agua*factor, " taza/s de agua")    