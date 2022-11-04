import platform,time
print ("Obteniendo datos de tu PC")
print ("Por favor espere...")

time.sleep(3)
    
print ("Nombre del sistema operativo:", platform.system())
print ("Versión del sistema operativo: ",platform.release())
print ("Datos del microprocesador",platform.processor())
print ("Indica si la arquitectura",platform.architecture())