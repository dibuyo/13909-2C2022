#Trabajo Practico Obligatorio Nro. 3
#Version sin librerias y sin caracteres especiales como acentos.
#Martin Rivas

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
CYAN = '\033[36m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'

INT = 1
FLOAT = 2
STRING = 3
BOOL = 4
LIST = 5

internet = 0
computadoras = 0
mayor_compus = 0
mayor_legajo = 0
mayor_nombre  = ""
mayor_apellido = ""
cantidad = 0
tipo_casa = 0
tipo_depto = 0
edades_promedio = 0

def main():
    _private_cls()
    global BLACK, RED, GREEN, YELLOW, BLUE, CYAN, WHITE, UNDERLINE, RESET
    menu()

        
def bienvenida():
    _private_cls()
    print(YELLOW + "Trabajo Practico Obligatorio Nro. 3")
    print(GREEN + "Martin Rivas")
    print(RED + "Colegio de Lanus")
    print(RESET)

def menu():
    while True:
        bienvenida()
        print(BLUE + "1 - Iniciar Censo")
        print("2 - Mostrar Resultados")
        print("3 - Salir")
        print(RESET)
        opt = _private_input("Seleccione una Opcion: ", INT)
        if(opt == 1):
            census()
            census_restart()
        elif(opt == 2 ):
            finilizar()
        elif(opt == 3):
            break

def census_restart():
    while True:
        _private_cls()
        print(BLUE)
        continuar = _private_input("Quiene continuar con el censo estudiantil?", BOOL)
        print(RESET)
        if( continuar == 0 ):
            break
        else:
            census()

def census():
    global cantidad, edades_promedio, internet, computadoras, mayor_apellido, mayor_legajo, mayor_nombre, mayor_compus, tipo_casa, tipo_depto
    _private_cls()
    legajo = 0
    nombre = ""
    apellido = ""
    edad = 0
    tiene_compu = 0
    cuantas = 0

    legajo = _private_input("Numero de Legajo:", INT)

    nombre = _private_input("Nombre del alumno:", STRING)

    apellido = _private_input("Apellido del alumno:", STRING)

    edad = _private_input("Edad:", INT, [], 99)
    edades_promedio += edad

    if( _private_input("Tiene Internet?", BOOL) == 1 ):
        internet += 1

    tiene_compu = _private_input("Tiene Computadora?", BOOL)

    if( tiene_compu == 1 ):
        cuantas = _private_input("Cuantas computadoras:", INT)
        computadoras += cuantas
        if( cuantas > mayor_compus ):
            mayor_compus = cuantas
            mayor_legajo = legajo
            mayor_nombre  = nombre
            mayor_apellido = apellido

    tipo_vivienda = _private_input("Tipo de Vivienda:", LIST, ["Casa", "Dpto"])
    if( tipo_vivienda == 1):
        tipo_casa += 1
    elif(tipo_vivienda == 2):
        tipo_depto += 1

    cantidad += 1

def finilizar():
    _private_cls()
    
    if( cantidad < 1):
        print(RED)
        print("No hay informacion cargada para el Censo.")
        print(RESET)
        input("Oprimir cualquier tecla para continuar...")
        return

    print("Resultado del censo")
    print(YELLOW)
    print("Cantidad de Alumnos con Internet: {}".format( internet ))
    print("Cantidad de Alumnos con computadoras: {}".format( computadoras ))
    print("Alumno mas computadoras: ({}) {}, {} tiene {}".format(mayor_legajo, mayor_nombre, mayor_apellido, mayor_compus ))
    print(BLUE)
    print("Distribucion tipo vivienda:")
    print(" - Casa: {}%".format(round(tipo_casa/cantidad*100)))
    print(" - Depto: {}%".format(round(tipo_depto/cantidad*100)))
    print("Promedio Edad: {}".format(round(edades_promedio/cantidad),1))
    print(RESET)
    input("Oprimir cualquier tecla para continuar...")

def _private_input(pregunta, tipo, lista = [], max = 999999):
    tmp = ""

    #Defino un Maximo por si me pasan como parametro
    if( max != 999999):
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

        #Funcion isnumeric no me funciono en python 2.
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

def _private_cls():
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == "__main__":
    main()