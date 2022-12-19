#Examen Final de Programación Python
#Alumno: Martin Rivas
#Docente: Lic. Patricia Tucci

import os

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

INT = 1
FLOAT = 2
STRING = 3
BOOL = 4
LIST = 5

vac_qty = 0
vac_masculino = 0
vac_femenino = 0
vac_femenino_edades = 0
vac_masculino_mayores_60_5_dosis = 0
vac_menor_edad = 105
vac_menor_dni = 0
vac_menor_nombre = ""
vac_menor_apellido = ""

def main():
    global RED, GREEN, YELLOW, BLUE, RESET
    _private_cls()
    menu()

def bienvenida():
    global GREEN, YELLOW, BLUE, RESET
    _private_cls()
    print(YELLOW + "13909-Trayecto Tecnológico: Introducción a la programación")
    print(BLUE + "Software libre 2c2022")
    print(GREEN + "Martin Rivas")
    print(RESET)

def menu():
    while True:
        bienvenida()
        print(BLUE + "1 - Iniciar proceso de Vacunación")
        print("2 - Mostrar Resultados del día")
        print("3 - Salir")
        print(RESET)
        opt = _private_input("Seleccione una Opcion: ", INT)
        if(opt == 1):
            vacunacion()
        elif(opt == 2 ):
            estadisticas()
        elif(opt == 3):
            break

def vacunacion():
    while True:
        _private_cls()
        print(BLUE)
        continuar = _private_input("¿Hay Personas para vacunar?", BOOL)
        print(RESET)
        if( continuar == 0 ):
            break
        else:
            cargar_datos()

def cargar_datos():
    global vac_qty, vac_masculino, vac_femenino, vac_femenino_edades, vac_masculino_mayores_60_5_dosis, vac_menor_edad, vac_menor_dni, vac_menor_nombre, vac_menor_apellido
    _private_cls()

    dni = 0
    nombre = ""
    apellido = ""
    edad = 0
    genero = ""
    vacuna = ""

    dni = _private_input("Número de DNI del vacunado:", INT)
    apellido = _private_input("Apellido del vacunado:", STRING)
    nombre = _private_input("Nombre del vacunado:", STRING)
    genero = _private_input("Genero del Vacunado:", LIST, ["Femenino", "Masculino"])
    edad = _private_input("Edad del vacunado:", INT, [], 105)
    vacuna = _private_input("Dosis:", LIST, ["4º dosis", "5º dosis"])

    vac_qty += 1
    #1º Femenino
    if( genero == 1):
        vac_femenino += 1
    else:
        vac_masculino +=1 

    if( genero == 1 ):
        vac_femenino_edades += edad
    elif( edad > 60 and vacuna == 2 ): #2 es Quinta dosis
        vac_masculino_mayores_60_5_dosis += 1
    
    if( edad < vac_menor_edad ):
        vac_menor_edad = edad
        vac_menor_dni = dni
        vac_menor_nombre = nombre
        vac_menor_apellido = apellido

def estadisticas():
    global GREEN, YELLOW, BLUE, RESET
    global vac_qty, vac_masculino, vac_femenino, vac_femenino_edades, vac_masculino_mayores_60_5_dosis, vac_menor_edad, vac_menor_dni, vac_menor_nombre, vac_menor_apellido
    _private_cls()

    if( vac_qty < 1):
        print(RED)
        print("No hay informacion cargada de personas vacunadas.")
        print(RESET)
        input("Oprimir cualquier tecla para continuar...")
        return

    print(BLUE + "Estadisticas del día")
    print(RESET)
    print("Cantidad de vacunados Femeninos: {}".format( vac_femenino ))
    print("Cantidad de vacunados Masculino: {}".format( vac_masculino ))

    if( vac_femenino > 0 ):
        print(GREEN + "Promedio Edad Mujeres Vacunadas: {}".format( vac_femenino_edades / vac_femenino) )
    else:
        print(GREEN + "Promedio Edad Mujeres Vacunadas: {}".format( 0 ) )
    print(RESET)

    print(YELLOW + "Cantidad de varones mayores 60 años que se aplicaron 5º dosis: {}".format( vac_masculino_mayores_60_5_dosis ) )
    print(RESET)

    print(BLUE + "La persona más joven que se vacuno hasta ahora: ")
    print("Nombre: {}".format(vac_menor_nombre))
    print("Apellido: {}".format(vac_menor_apellido))
    print("DNI: {}".format(vac_menor_dni))

    input(BLUE + "Oprimir cualquier tecla para continuar...")
    print(RESET)

def _private_input(pregunta, tipo, lista = [], max = 99999999):
    tmp = ""

    #Defino un Maximo por si me pasan como parametro el DNI maximo podría ser el más grande.
    if( max != 99999999):
        pregunta += "(MAX:{})".format(max)

    if( tipo == BOOL):
        pregunta = pregunta + "(0 - NO / 1 - SI)" 
    elif( tipo == LIST ):
        pregunta = pregunta + "("
        for i in range(len(lista)):
            if (i > 0 ): pregunta += "|"
            pregunta += "{}-{}".format(i+1,lista[i])
        pregunta = pregunta + ")"

    while True:
        tmp = str(input(pregunta))

        if( tipo == INT and tmp.isdigit() and max >= int(tmp) ):
            return int(tmp)
        elif( tipo == FLOAT and tmp.isdigit() ):
            return float(tmp)
        elif( tipo == STRING ):
            return tmp
        elif( tipo == BOOL and tmp.isdigit() and int(tmp) <= 1 ):
            if( int(tmp) > 0): 
                return 1
            else:
                return 0
        elif( tipo == LIST and tmp.isdigit() and int(tmp) > 0 and int(tmp) <= len(lista) ):
            return int(tmp)

        print(RED)
        print("Los datos ingresados no son válidos. Vuelva a ingresar el dato.")
        print(RESET)

def _private_cls():
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == "__main__":
    main()