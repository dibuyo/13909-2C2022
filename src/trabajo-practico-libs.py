import sys
import time
import pickle
import os

from enum import Enum, IntEnum
from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *
from colors import color

class Tipos(Enum): 
    INT = 1
    FLOAT = 2
    STRING = 3
    BOOL = 4
    LIST = 5

class TipoVivienda(IntEnum): 
    CASA = 1
    DEPTO = 2

class Alumno:
  def __init__(self, l, n, a, e, i, c, v):
    self.legajo = l
    self.nombre = n
    self.apellido = a
    self.edad = e
    self.internet = i
    self.computadoras = c
    self.vivienda = v

censados = []

def main():
    global censados

    menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.HEAVY_BORDER) \
        .set_prompt(">") \
        .set_title_align('center') \
        .set_subtitle_align('center') \
        .set_left_margin(2) \
        .set_right_margin(2) \
        .show_header_bottom_border(True)

    menu = ConsoleMenu("Trabajo Practico Obligatorio Nro. 3\n{}".format(color("Martin Rivas", fg='red')), "{}".format(color("Colegio de Lanus", fg='yellow')), formatter=menu_format)

    menu_censar = FunctionItem("Iniciar Proceso de Censo Estudiantil", iniciar)
    menu_cargar = FunctionItem("Recuperar informacion de archivo", load)

    submenu = ConsoleMenu("{}".format(color("Colegio de Lanus", fg='yellow')), "Reportes disponibles",
                            prologue_text="Listado de opciones disponibles para generar reportes sobre la información capturada del Censo de los alumnos.",
                            epilogue_text="Seleccionar una Opcion disponible para mostrar el reporte.",
                            formatter=MenuFormatBuilder()
                            .set_title_align('center')
                            .set_subtitle_align('center')
                            .set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_BORDER)
                            .show_prologue_top_border(True)
                            .show_prologue_bottom_border(True))

    submenu.append_item(FunctionItem("Internet en hogares.", internet, [3]))
    submenu.append_item(FunctionItem("Computadora en hogares.", computer, [3] ))
    submenu.append_item(FunctionItem("Alumno con mas computadoras.", computer_top, [3]))
    submenu.append_item(FunctionItem("Distribucion tipo de vivienda.", vivinda, [3]))
    submenu.append_item(FunctionItem("Promedio de Edades.", edades, [3]))
    submenu.append_item(FunctionItem("Resumen.", resumen, [5]))

    reportes = SubmenuItem("Reportes", submenu=submenu)
    
    menu.append_item(menu_censar)
    menu.append_item(reportes)
    menu.append_item(menu_cargar)

    menu.start()
    menu.join()

def iniciar():
    while True:
        if( len(censados) > 0 ):
            if( _private_input("¿Quiere seguir censando alumnos?", Tipos.BOOL) == 0 ):
                break
            else:
                _private_cls()
        census()

def census():
    legajo = 0
    nombre = ""
    apellido = ""
    edad = 0
    tiene_internet = 0
    tiene_compu = 0
    cuantas = 0

    legajo = _private_input("Numero de Legajo:", Tipos.INT)

    nombre = _private_input("Nombre del alumno:", Tipos.STRING)

    apellido = _private_input("Apellido del alumno:", Tipos.STRING)

    edad = _private_input("Edad:", Tipos.INT, [], 99)

    tiene_internet = _private_input("Tiene Internet?", Tipos.BOOL)

    tiene_compu = _private_input("Tiene Computadora?", Tipos.BOOL)

    if( tiene_compu == 1 ):
        cuantas = _private_input("Cuantas computadoras:", Tipos.INT)

    tipo_vivienda = _private_input("Tipo de Vivienda:", Tipos.LIST, ["Casa", "Dpto"])
    
    censados.append( Alumno(legajo, nombre, apellido, edad, tiene_internet, cuantas, tipo_vivienda) )
    _private_save("data/censo.dat")

def resumen(timeout):
    if( len(censados) > 0):
        internet(0)
        computer(0)
        computer_top(0)
        vivinda(0)
        edades(0)
    else:
        print(color("No hay ningun alumno censado.", fg='red'))
    time.sleep(timeout)

def internet(timeout):
    internet = 0
    for a in censados:
        internet += a.internet

    print("Hay {} Alumnos con Internet en sus casas.".format(color(internet, fg='yellow')))
    time.sleep(timeout)

def computer(timeout):
    computadoras = 0
    for a in censados:
        computadoras += a.computadoras

    print("Hay {} computadoras entre todos los alumnos censados.".format(color(computadoras, fg='green')))
    time.sleep(timeout)

def computer_top(timeout):
    max = 0
    al = {}

    for a in censados:
        if( a.computadoras > max ):
            al = a

    if( len(censados) > 0):
        print("Alumno mas computadoras: ({}) {}, {} tiene {} computadoras".format(color(al.legajo, fg='green'), al.nombre, al.apellido, color(al.computadoras, fg='green')))
    else:
        print(color("No hay ningun alumno censado.", fg='red'))
    time.sleep(timeout)

def vivinda(timeout):
    print("Distribucion tipo vivienda:")

    cantidad = len(censados)
    casas = 0
    dpto = 0
    for a in censados:
        if( a.vivienda == TipoVivienda.CASA ):
            casas += 1
        elif( a.vivienda == TipoVivienda.DEPTO ):
            dpto += 1

    print(" - Casa: {}%".format(color(round(casas/cantidad*100), fg='green')))
    print(" - Depto: {}%".format(color(round(dpto/cantidad*100), fg='green')))

    time.sleep(timeout)

def edades(timeout):
    cantidad = len(censados)
    edades_promedio = 0
    for a in censados:
        edades_promedio += a.edad

    print("Promedio Edad: {}".format(color(round(edades_promedio/cantidad),1), fg='green'))

    time.sleep(timeout)    

def load():
    print("Cargar datos desde Archivos")
    _private_load("data/censo.dat")
    time.sleep(1)

def _private_input(pregunta, tipo, lista = [], max = 999999):
    tmp = ""

    #Defino un Maximo por si me pasan como parametro
    if( max != 999999):
        pregunta += "(MAX:{})".format(max)

    if( tipo == Tipos.BOOL):
        pregunta = pregunta + "(0 - NO / 1 - SI)" 
    elif( tipo == Tipos.LIST ):
        pregunta = pregunta + "("
        for i in range(len(lista)):
            if (i > 0 ): pregunta += "|"
            pregunta += "{}-{}".format(i+1,lista[i])
        pregunta = pregunta + ")"

    while True:
        tmp = str(input(pregunta))

        #Funcion isnumeric no me funciono en python 2.
        if( tipo == Tipos.INT and tmp.isdigit() and max >= int(tmp) ):
            return int(tmp)
        elif( tipo == Tipos.FLOAT and tmp.isdigit() ):
            return float(tmp)
        elif( tipo == Tipos.STRING ):
            return tmp
        elif( tipo == Tipos.BOOL and tmp.isdigit() and int(tmp) <= 1 ):
            if( int(tmp) > 0): 
                return 1
            else:
                return 0
        elif( tipo == Tipos.LIST and tmp.isdigit() and int(tmp) > 0 and int(tmp) <= len(lista) ):
            return int(tmp)

def _private_cls():
    os.system('cls' if os.name=='nt' else 'clear')

def _private_save(fspath):
    with open(fspath, "wb") as f:
        for s in censados:
            pickle.dump(s, f)
        f.close

def _private_load(fspath):
    cargas = 0
    if( not os.path.exists(fspath) ):
        print("{}".format(color("No se encontro el archivo", fg='red')))
        return

    with open(fspath,"rb") as f:
        while True:
            try:
                censados.append(pickle.load(f))
                cargas += 1
            except EOFError:
                break

    print("Se cargaron {} registros.".format(color(cargas, fg='yellow')))
    time.sleep(1)

if __name__ == "__main__":
    main()