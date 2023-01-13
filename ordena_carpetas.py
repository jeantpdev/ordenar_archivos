import os
import shutil
import errno
from getpass import getuser

ext_texto = ['.docx', '.txt', '.doc','.pdf', '.pptx']
ext_imagenes = ['.png', '.jpg', '.jpeg', '.gif']
ext_video = ['.mov', '.mp4']

usuario = getuser()

#if os.path.isdir(f'C:\\Users\\{usuario}\\Downloads\\'):
#    print('La carpeta existe.');
#    ruta_descargas = f'C:\\Users\\{usuario}\\Downloads\\'
#    print(ruta_descargas)
#else:
#    ruta_descargas = f'C:\\Usuarios\\{usuario}\\Descargas\\'
#    print('No existe')

def ordenar (archivo, ext, ruta_descargas):
    for i in ext_texto:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_descargas + 'Texto')

    for i in ext_video:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_descargas + 'Videos')      

    for i in ext_imagenes:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_descargas + 'Imagenes')

def crear_carpetas():
    try:
        os.mkdir(ruta_descargas+'Texto')
        os.mkdir(ruta_descargas+'Videos')
        os.mkdir(ruta_descargas+'Imagenes')
        os.mkdir(ruta_descargas+'Otros')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
#def main():
    #crear_carpetas()
    #for archivo in os.listdir(ruta_descargas):       
        #nombre_archivo, ext = os.path.splitext(archivo)
        #ordenar(archivo, ext, ruta_descargas)

if __name__ == '__main__':

    usuario = getuser()

    if os.path.isdir(f'C:\\Users\\{usuario}\\Downloads\\'):
        print('La carpeta existe.')
        ruta_descargas = f'C:\\Users\\{usuario}\\Downloads\\'
        print(ruta_descargas)
    else:
        ruta_descargas = f'C:\\Usuarios\\{usuario}\\Descargas\\'
        print('No existe')



