#Ejercicio B
# Se ingresan los sueldos de dos integrantes de una familia y se pretende averiguar si deben cobrar 
# o no la asignación familiar por hijo. Si el sueldo de alguno de los dos integrantes es superior a $105.139 
# se excluye del cobro de la asignación al grupo familiar. 
# Lo mismo sucederá si la suma de ambos ingresos superan los $210.278. 
# Mostrar si les corresponde o no cobrar la Asignación familiar por hijo.

print("""
Clase 9 - Ejercicio B
Actividad obligatoria - Martín Rivas
""")

sueldo = total = 0
asignacion = 1
tmp = ""
SUELDO_MAX_AUH = 105139.0

for i in range(1,3):
    while sueldo == 0:
        tmp = str(input("Ingrese el #"+str(i)+" sueldo del grupo familiar: "))
        #Funcion isnumeric no me funciono en python 2.
        if tmp.isdigit():
            sueldo = float(tmp)
    total += sueldo
    if sueldo > SUELDO_MAX_AUH or total > SUELDO_MAX_AUH*i:
        asignacion = 0
    sueldo = 0

print("Total ingreso: $", total, " Tope maximo: $", SUELDO_MAX_AUH*i)
if asignacion == 1:
    print("Puede solicitar el AUH ya que el sueldo familiar esta dentro del maximo permitido." )
else:
    print("No corresponde cobrar AUH.")