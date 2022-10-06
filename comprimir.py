
import os
import sys
import zipfile

# Funcion para comprimir un directorio
def zip_directory(path_zip, filename):
    
    zipf = zipfile.ZipFile( filename, 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(path_zip):
        for file in files:
            zipf.write(os.path.join(root, file))

    zipf.close()

# Funcion para descomprimir un fichero zip
def unzip_directory( path_unzip, filename):

    with zipfile.ZipFile( filename, 'r') as zip_ref:
       zip_ref.extractall( path_unzip)

# Mostramos el contenido de un fichero Zip
def zip_view( filename):

     with zipfile.ZipFile( filename) as file:
        file.printdir()


# Ayuda para usar el script
def help():
    print(""" Wrong parameter:
    
    Usage:
        python zip-directory.py Zip path filename       # To zip directory recursively
        python zip-directory.py UnZip path filename     # To un Zip
        python zip-directory.py View filename           # To view files in zip archive

    """)


# Inicio del programa
#
if __name__ == '__main__':      

    # Comprobamos si pasan algun paramentro, si no hay parametro salta al mensaje de error
    #
    if len(sys.argv) > 1:
        
        # Si el primer parametro es la palabra "Zip" => Comprimimos
        #
        if ( sys.argv[1] == 'Zip'):

            # Revisamos los dos siguiente parametros que se han entrado para obtener
            # la ruta a zipear y el nombre que le daremos al archivo zip
            #
            # Aqui se tendria que colocar la validación para que en caso de que estos dos
            # parametros no viniera generará una alerta o error
            #
            filename =  sys.argv[3]
            path =  sys.argv[2]

            # Escribimos por pantalla que va realizar el script
            print( sys.argv[1] + ": directory: " + path + " into file: " + filename)

            # Llamamos a la funcion que zipea
            zip_directory( path, filename)

         # Si el primer parametro es la palabra "UnZip" => Descomprimimos
         #
        elif( sys.argv[1] == 'UnZip'):

            # Revisamos los dos siguiente parametros que se han entrado para obtener
            # la ruta donde descomprimiremos y el fichero a descomprimir
            #
            # Aqui se tendria que colocar la validación para que en caso de que estos dos
            # parametros no viniera generará una alerta o error
            #
            filename =  sys.argv[3]
            path =  sys.argv[2]

            # Escribimos por pantalla que va realizar el script
            print( sys.argv[1] + ": file: " + filename + " directory: " + path)

            # LLamamos a la función para descomprimir
            unzip_directory( path, filename)
        
        # Si el primer parametro es la palabra "View" => Ver contenido del fichero zip
         #
        elif( sys.argv[1] == 'View'):

            # Solo requiere un parametro mas que es el nombre del fichero zip
            #
            # Aqui se tendria que colocar la validación para que en caso de que estos dos
            # parametros no viniera generará una alerta o error
            #
            filename =  sys.argv[2]

            # Escribimos por pantalla que va realizar el script
            print( sys.argv[1] + ": file: " + filename )

            # Llamamos a la función para visualizar el fichero
            zip_view( filename)

        else:
            # Llamamos a la función de mostrar la ayuda
            #
            print( sys.argv[1] + ": unknown command")
            help()
            
    else:
        # Llamamos a la función de mostrar la ayuda
        #
        print( "Unknown command")
        help()


    sys.exit()
