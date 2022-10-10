import sys
import os
import platform
import glob

path = "./src/"
extension = ".py"
program = ""
fsprogram = ""
version = platform.python_version()

print("UNLA - Introducción a la programación: Software libre (13909)")
print("Bienvenido a Python (13909)")
print("Version de Pyhton: " + version)

if len(sys.argv) > 1 :
    program = sys.argv[1]

if program[-3:] != ".py" :
    fsprogram = program + ".py"
else:
    fsprogram = program

fspathProgram = path+"*"+extension
fspath = path+fsprogram
isExist = os.path.exists(fspath)

if isExist :
    if( int(version.split(".")[0]) < 3):
        execfile(fspath)
    else:
        #sys.path.append(path)
        #modules = [ program ]
        #map(__import__, modules)
        code = open(fspath).read()
        exec(code.encode('ascii', 'ignore'))
else:
    actividades = []
    for file in glob.glob(fspathProgram):
        actividades.append(file)
    print("No se encontro la actividad. Estan disponibles las siguientes actividades:")
    print(actividades)