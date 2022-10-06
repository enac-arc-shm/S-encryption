#instalar pynput / pip install 
from pynput import keyboard as kb
from gui import *
from operaciones import *
from organizar import *
import time
op = 0
escuchar = True


def getop():
	global op
	return op

def setop(_op):
	global op
	op = _op

def getescuchar():
	global escuchar
	return escuchar

def setescuchar(booleand):
	global escuchar
	escuchar = booleand

def pulsa(tecla):
	clearConsole()
	if str(tecla) == 'Key.enter':
		print("Opciòn ", getop(), " seleccionada")
		#setescuchar(False)
		accion()
	else:
		if str(tecla) == 'Key.ctrl':
			exit()
		opt = select(str(tecla),getop())
		setop(opt)
		#print (opt)
		mostrarmenu(getop())

def accion():
	if getop() == 0:
		clearConsole()
		organizarcarpetas()
	elif getop() == 1:
		clearConsole()
		encriptararchivo()
	elif getop() == 2:
		clearConsole()
		desencriptararchivo()
	elif getop() == 3:
		clearConsole()
		imprimirmenuinforme()
	elif getop() == 4:
		clearConsole()
		organizar()
	imprimirmenu()

def accioninfo():
	if getop() == 0:
		clearConsole()
		verinformecompleto()
	elif getop() == 1:
		clearConsole()
		verinforme()
	imprimirmenu()

def imprimirmenu():
	setop(select('', getop()))
	mostrarmenu(getop())
	escuchador = kb.Listener(pulsa)
	escuchador.start()
	while escuchador.is_alive():
		if getescuchar():
			pass
		else: 
			escuchador.stop()
#Ver menu
def imprimirmenuinforme():
	setop(selectopinfo('', 0))
	opcionesinforme(getop())
	escuchador = kb.Listener(pulsa1)
	escuchador.start()
	while escuchador.is_alive():
		#if getescuchar():
		pass
		#else: 
			#escuchador.stop()
	

def pulsa1(tecla):
	clearConsole()
	if str(tecla) == 'Key.enter':
		accioninfo()
	else: 
		opt = selectopinfo(str(tecla),getop())
		setop(opt)
		#print (opt)
		opcionesinforme(getop())
	

if __name__ == "__main__":
	imprimirmenu()