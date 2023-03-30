import os
import errno
import shutil
from getpass import getuser

ext_texto = ['.docx', '.txt', '.doc','.pdf', '.pptx']
ext_imagenes = ['.png', '.jpg', '.jpeg', '.gif']
ext_video = ['.mov', '.mp4', '.mkv']
ext_archivos = ['.rar','.zip']
usuario = getuser()

def crear_carpetas(ruta_descargas):

    try:
        if ruta_descargas+'Texto' == True:
            print("Carpeta texto existe")
        else:
            os.mkdir(ruta_descargas+'Texto')
            print("Carpeta texto creada")

        if ruta_descargas+'Videos' == True:
            print("Carpeta videos Existe")
        else:
            os.mkdir(ruta_descargas+'Videos')
            print("Carpeta videos creada")

        if ruta_descargas+'Imagenes' == True:
            print("Carpeta imagenes Existe")
        else:
            os.mkdir(ruta_descargas+'Imagenes')
            print("Carpeta imagenes creada")

        if ruta_descargas+'Otros' == True:
            print("Carpeta otros Existe")
        else:
            os.mkdir(ruta_descargas+'Otros')
            print("Carpeta otros creada")

    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def nosexd():
    for archivo in os.listdir(ruta_descargas):       
        nombre_archivo, ext = os.path.splitext(archivo)
        ordenar(nombre_archivo, ext, ruta_descargas)

def existe_ruta():

    usuario = getuser()

    #Se comprueba que exista la carpeta descargas para el idioma inglés
    if os.path.isdir(f'C:\\Users\\{usuario}\\Downloads\\'):
        ruta_descargas = f'C:\\Users\\{usuario}\\Downloads\\'
        print(ruta_descargas)
        return ruta_descargas
    else:
        ruta_descargas = f'C:\\Usuarios\\{usuario}\\Descargas\\'
        print(ruta_descargas)
        return ruta_descargas

def ordenar (archivo, ext, ruta_descargas):
    for i in ext_texto:
        if ext == i:
            shutil.move(ruta_descargas + archivo+ext, ruta_descargas + 'Texto')

    for i in ext_video:
        if ext == i:
            shutil.move(ruta_descargas + archivo+ext, ruta_descargas + 'Videos')      

    for i in ext_imagenes:
        if ext == i:
            shutil.move(ruta_descargas + archivo+ext, ruta_descargas + 'Imagenes')

    for i in ext_archivos:
        if ext == i:
            shutil.move(ruta_descargas + archivo+ext, ruta_descargas + 'Otros')

if __name__ == '__main__':

    ruta_descargas = existe_ruta()
    crear_carpetas(ruta_descargas)
    nosexd()


