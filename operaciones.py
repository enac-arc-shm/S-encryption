#pip instal rsa, pip install keyboard, pip install werkzeug, pip install pynput
import os
import glob
import getpass
import shutil
import rsa
import keyboard
from pathlib import Path
from cryptography.fernet import Fernet
from werkzeug.security import generate_password_hash, check_password_hash
from main import *
from gui import *
from datetime import date
from datetime import datetime
from itertools import islice
main_password_encrypted = 'pbkdf2:sha256:30$yN4grWDimYv9N88VoKxcykjpnjFmKbJD10bTeLP0iPAlAlxFKvR60Offv3F4nTcFPyHnAUDFIDSN4C3fzlpwwNKMgDahOBePiB1B$c8fe00430ea49f2c0ee59f59a68bd7e8c3274804c6b96ec21711c3a245ad2c1b'
#enctex = rsa.encrypt(contraseña.encode(),pubkey)

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

extensions = {
    "jpg": "IMAGENES",
    "png": "IMAGENES",
    "ico": "IMAGENES",
    "gif": "IMAGENES",
    "svg": "IMAGENES",
    "jpeg": "IMAGENES",
    "sql": "SQL",
    "exe": "PROGRAMS",
    "msi": "PROGRAMS",
    "pdf": "PDF",
    "xlsx": "EXCEL",
    "csv": "EXCEL",
    "rar": "ARCHIVE",
    "zip": "ARCHIVE",
    "gz": "ARCHIVE",
    "tar": "ARCHIVE",
    "docx": "WORD",
    "torrent": "TORRENT",
    "txt": "TEXT",
    "ipynb": "PYTHON",
    "py": "PYTHON",
    "pptx": "POWERPOINT",
    "ppt": "POWERPOINT",
    "mp3": "AUDIO",
    "wav": "AUDIO",
    "mp4": "VIDEO",
    "m3u8": "VIDEO",
    "webm": "VIDEO",
    "ts": "VIDEO",
    "json": "JSON",
    "css": "WEB",
    "js": "WEB",
    "html": "WEB",
    "apk": "APK",
    "deb": "APK",
    "sqlite3": "sqlite3",
}

def encriptar_archivo(_RUTA_, _NOMBRE_):
    with open(f'{_RUTA_}/filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(f'{_RUTA_}/{_NOMBRE_}', 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(f'{_RUTA_}/{_NOMBRE_}', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print(f"[+]Archivo <{_RUTA_}/{_NOMBRE_}> encriptado")
    informe(f"[+]Archivo <{_RUTA_}/{_NOMBRE_}> encriptado")

def desencriptar_archivo(_RUTA_, _NOMBRE_):
    with open(f'{_RUTA_}/filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(f'{_RUTA_}/{_NOMBRE_}', 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(f'{_RUTA_}/{_NOMBRE_}', 'wb') as dec_file:
        dec_file.write(decrypted)
    print(f"[+]Archivo <{_RUTA_}/{_NOMBRE_}> desencriptado")
    informe(f"[+]Archivo <{_RUTA_}/{_NOMBRE_}> desencriptado")

def verificar_key(_RUTA_):
	if os.path.isfile(f'{_RUTA_}/filekey.key'):
		print('[*]Leyendo llave de cifrado')
		informe('[*]Leyendo llave de cifrado')
	else:
		print('[-]No se encontro la llave de cifrado, generando llave')
		informe('[-]No se encontro la llave de cifrado, generando llave')
		key = Fernet.generate_key()
		with open(f'{_RUTA_}/filekey.key', 'wb') as filekey:
			filekey.write(key)

def verificar_llaves(_RUTA_):
    pubkey, privkey = rsa.newkeys(1024)
    print(pubkey, privkey)
    if os.path.isfile(f'{_RUTA_}/pubkey.key'):
    	print('[*]Leyendo llave publica')
    else:
    	print('[-]No se encontro la llave publica, generando llave')
    	with open(f'{_RUTA_}/pubkey.key', 'wb') as pubkey:
    		pubkey.write(pubkey)
    if os.path.isfile(f'{_RUTA_}/privkey.key'):
    	print('[*]Leyendo llave privada')
    else:
    	print('[-]No se encontro la llave privada, generando llave')
    	with open(f'{_RUTA_}/privkey.key', 'wb') as privkey:
    		privkey.write(privkey)

def solicitar_ruta():
    while True:
        RUTA = input('[?]Ingrese la ruta:')
        if RUTA == "":
            print('[-]Ingrese una ruta')
        else: 
            break
    return RUTA

def solicitar_ruta_archivo(_accion_):
    while True:
        RUTA = input(f'[?]Ingrese la ruta del archivo a {_accion_}:')
        if RUTA == "":
            print('[-]Ingrese una ruta')
        else: 
            break
    return RUTA

def organizarcarpetas():
    rsa = input('')
    Ruta = solicitar_ruta()
    organize_junk(Ruta)
    nothing = input('Presiona ENTER para regresar al menu...')
    clearConsole()

def comprimir():
    rsa = input('')
    Ruta = solicitar_ruta()

def encriptararchivo():
    rsa = input('')
    Ruta = solicitar_ruta_archivo('encriptar')
    verificar_key(Ruta)
    nombre = input('[?]Ingrese el nombre del archivo a encriptar:')
    if autentificar():
        encriptar_archivo(Ruta, nombre)
    else: 
        print("[-]Contraseña incorrecta")
    nothing = input('Presiona ENTER para regresar al menu...')
    clearConsole()

def desencriptararchivo():
    rsa = input('')
    Ruta = solicitar_ruta_archivo('desencriptar')
    verificar_key(Ruta)
    nombre = input('[?]Ingrese el nombre del archivo a desencriptar:')
    if autentificar():
        desencriptar_archivo(Ruta, nombre)
    else:
        print("[-]Contraseña incorrecta")
    nothing = input('Presiona ENTER para regresar al menu...')
    clearConsole()


def verinformecompleto():
    rsa = input('')
    rsa = input('')
    with open("informe.txt","r") as archivo:
            print(archivo.read())
      
    continuar = input('Presiona ENTER para regresar al menu...')
    clearConsole()


def verinforme():
    rsa = input('')
    rsa = input('')
    n = input('[?]Ingrese el nùmero de lineas que quiere ver: ')
    with open("informe.txt","r") as archivo:
            for lineas in islice(archivo, int(n)):
                print(lineas, end='')
    nothing = input('Presiona ENTER para regresar al menu...')
    clearConsole()
    

def organize_junk(_RUTA_):
	#print(rsa.encrypt(password.encode(),pubkey))
    #main_password_usr = rsa.encrypt(password.encode(),pubkey)
    #print(rsa.encrypt('sergio'.encode(),pubkey))
    if autentificar():
    		print("[+]Contraseña correcta")
    		path = _RUTA_
    		verbose = 0
    		for extension, folder_name in extensions.items():
	           	 # get all the files matching the extension
	           	 files = glob.glob(os.path.join(path, f"*.{extension}"))
	           	 print(f"[*] Found {len(files)} files with {extension} extension")
	           	 informe(f"[*] Found {len(files)} files with {extension} extension")
	           	 if not os.path.isdir(os.path.join(path, folder_name)) and files:
			             # create the folder if it does not exist before
	                 	print(f"[+] Making {folder_name} folder")
	                 	informe(f"[+] Making {folder_name} folder")
       		         	os.mkdir(os.path.join(path, folder_name))
	           	 for file in files:
	           	 # for each file in that extension, move it to the correponding folder
	           		 basename = os.path.basename(file)
	           		 dst = os.path.join(path, folder_name, basename)
	           		 if verbose:
	           		        print(f"[*] Moving {file} to {dst}")
	           		        informe(f"[*] Moving {file} to {dst}")
	           		 shutil.move(file, dst)
    else:
        print("[-]Contraseña incorrecta")

def autentificar():
    global main_password_encrypted
    #password = input('[?]Contraseña de adminstrador: ')
    password=getpass.getpass("Indica tu contraseña: ")
    #encriptadotext = generate_password_hash("sergio", 'pbkdf2:sha256:30', 100)
    return check_password_hash(main_password_encrypted, password)

def informe(_info_):
    fecha_registro = datetime.now()
    lineinfo = f'{_info_} {fecha_registro} \n' 
    archivo = open('informe.txt', 'a')
    archivo.write(lineinfo)
    archivo.close()

if __name__ == "__main__":
	encriptar_informe()