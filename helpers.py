import re # importo re para poder usar la funcion match que me permite validar el dni
import os # importo os para poder usar la funcion system que me permite limpiar la pantalla
import platform # importo platform para poder usar la funcion system que me permite limpiar la pantalla


def limpiar_pantalla(): # creo la funcion limpiar_pantalla que me permite limpiar la pantalla 
    os.system('cls') if platform.system() == "Windows" else os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None): # creo la funcion leer_texto que me permite leer un texto y validar que cumpla con la longitud minima y maxima que le pase por parametro
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto


def dni_valido(dni, lista): # creo la funcion dni_valido que me permite validar que el dni cumpla con el formato y que no este utilizado por otro cliente
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("DNI incorrecto, debe cumplir el formato.")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI utilizado por otro cliente.")
            return False
    return True
