##########################################################################################################
#   _____ ______ _   _ ______ _____            _____   ____  _____     _____  ______                     #
#  / ____|  ____| \ | |  ____|  __ \     /\   |  __ \ / __ \|  __ \   |  __ \|  ____|   diseñado por:    #
# | |  __| |__  |  \| | |__  | |__) |   /  \  | |  | | |  | | |__) |  | |  | | |__      Fabián Montero   #
# | | |_ |  __| | . ` |  __| |  _  /   / /\ \ | |  | | |  | |  _  /   | |  | |  __|            y         #
# | |__| | |____| |\  | |____| | \ \  / ____ \| |__| | |__| | | \ \   | |__| | |____    Julio Rodriguez  #
#  \_____|______|_| \_|______|_|__\_\/_/__  \_\_____/ \____/|_|  \_\  |_____/|______|___         _____   #
# | \ | |/ __ \|  \/  |  _ \|  __ \|  ____|/ ____|      /\   | |           /\    |___  /   /\   |  __ \  #
# |  \| | |  | | \  / | |_) | |__) | |__  | (___       /  \  | |          /  \      / /   /  \  | |__) | #
# | . ` | |  | | |\/| |  _ <|  _  /|  __|  \___ \     / /\ \ | |         / /\ \    / /   / /\ \ |  _  /  #
# | |\  | |__| | |  | | |_) | | \ \| |____ ____) |   / ____ \| |____    / ____ \  / /__ / ____ \| | \ \  #
# |_| \_|\____/|_|  |_|____/|_|  \_\______|_____/   /_/    \_\______|  /_/    \_\/_____/_/    \_\_|  \_\ #
#                                                                                                        #
##########################################################################################################
"""

"""
#------------------------------BIBLIOTECAS Y VARIABLES GLOBALES------------------------------#
from tkinter import *
import os.path
import random

global nm
nm = False

global mh
mh = False

global listaEstudiantesDIC
listaEstudiantesDIC = {}

global historial
historial = ""


#-------------------------------------------LÓGICA-------------------------------------------#
def nightMode():    #PASA A NIGHTMODE O A LIGHTMODE
    if nm == False:
        global nm
        nm = True
        main.configure(background = "#3F3F3F")
        labelRESULTADO.config(background = "#3F3F3F"  , foreground = "white")
        labelGRUPO.config(background = "#3F3F3F"  , foreground = "white")
        labelHISTORIAL.config(background = "#3F3F3F"  , foreground = "white")
        buttonGENERAR.config(background = "#e5e5e5")
        
    else:
        global nm
        nm = False
        main.configure(background = "#F0F0F0")
        labelRESULTADO.config(background = "#F0F0F0"  , foreground = "black")
        labelGRUPO.config(background = "#F0F0F0"  , foreground = "black")
        labelHISTORIAL.config(background = "#F0F0F0"  , foreground = "black")
        buttonGENERAR.config(background = "#F0F0F0")

def mostrarHistorial():     #MUESTRA U OCULTA EL HISTORIAL
    if mh == False:
        global mh
        mh = True
        labelHISTORIAL.config(text = "HISTORIAL\n" + historial)

    else:
        global mh
        mh = False
        labelHISTORIAL.config(text = "")

def crearGrupo():   #CEA UN GRUPO NUEVO
    #PIDE AL USUARIO EL NOMBRE DEL GRUPO NUEVO Y LOS ESTUDIANTES QUE LO INTEGRAN
    nombreGrupoNuevo = simpledialog.askstring("Crear Grupo" , "Nombre del grupo nuevo:              " , parent = main)
    nombreGrupoNuevo += ".txt"
    grupoNuevo = simpledialog.askstring("Crear Grupo" , "Introduzca una lista de estudiantes (nombres) separados por comas <,>." , parent = main)

    #CREA EL ARCHIVO DEL GRUPO NUEVO
    archivoGrupoNuevo = open(nombreGrupoNuevo , "w+")
    archivoGrupoNuevo.close()

    #GENERA EL TEXTO PARA ESCRIBIR EN EL ARCHIVO DEL GRUPO NUEVO
    contador = 1
    texto = ""
    for letra in grupoNuevo:
        if letra == ",":
            texto += "," + str(contador) + "\n"
            contador += 1

        else:
            texto += letra
    texto += "," + str(contador) + "\n"

    #ESCRIBE EN EL ARCHIVO DEL GRUPO NUEVO
    escribirAlFinal(nombreGrupoNuevo , texto)

    #ACTUALIZA LA INTERFAZ GRÁFICA
    labelGRUPO.config(text = "Grupo Actual:\n" + nombreGrupoNuevo[:-4])

    #GENERA EL DICCIONARIO CON LA LISTA DE LOS ESTUDIANTES
    global listaEstudiantesDIC
    listaEstudiantesDIC = {}
    nombre = ""
    numero = ""
    for letra in texto:
        if letra.isalpha():
            nombre += letra            

        elif letra.isdecimal():
            numero += letra

        elif letra == "\n":
            listaEstudiantesDIC[int(numero)] = nombre
            nombre = ""
            numero = ""

        else:
            None
    print(listaEstudiantesDIC)

def cargar():   #CARGA UN GRUPO EXISTENTE
    #LIMPIA EL HISTORIAL
    historial = ""
    
    #PIDE AL USUARIO LA UBICACION DEL ARCHIVO DEL GRUPO
    ubicacion = filedialog.askopenfilename(filetypes = (("TXT" , "*.txt") , ("CSV" , "*.csv")) , title = "Seleccione un archivo de grupo para cargar.")    

    #CARGA EL ARCHIVO CSV
    nombresCSV0 = open(ubicacion , "r")
    nombresCSV = nombresCSV0.read()  #STRING CON EL ARCHIVO CSV
    grupoActual = os.path.basename(ubicacion)#STRING CON EL NOMBRE DEL GRUPO ACTUAL
    grupoActual = grupoActual[:-4]

    #ACTUALIZA LA INTERFAZ GRÁFICA
    labelGRUPO.config(text = "Grupo Actual:\n" + grupoActual)

    #GENERA EL DICCIONARIO CON LA LISTA DE LOS ESTUDIANTES
    global listaEstudiantesDIC
    listaEstudiantesDIC = {}
    nombre = ""
    numero = ""
    for letra in nombresCSV:
        if letra.isalpha():
            nombre += letra            

        elif letra.isdecimal():
            numero += letra

        elif letra == "\n":
            listaEstudiantesDIC[int(numero)] = nombre
            nombre = ""
            numero = ""

        else:
            None
    print(listaEstudiantesDIC)

def generar():  #GENERA EL NOMBRE DE UN ESTUDIANTE AL AZAR
    global historial
    #GENERA UN NUMERO AL AZAR
    rango = len(listaEstudiantesDIC)
    resultado = random.randint(1 , rango)

    #GENERA UN NOMBRE USANDO EL NUMERO
    labelRESULTADO.config(text = str(listaEstudiantesDIC[resultado]))

    #ACTUALIZA EL HISTORIAL
    historial += str(listaEstudiantesDIC[resultado]) + "\n"
    mostrarHistorial()
    mostrarHistorial()

def escribirAlFinal(nombreArchivo , texto):    #EXCRIBE AL FINAL DEL ARCHIVO
    archivo = open(nombreArchivo , "r+")
    archivo.seek (0 , 2)
    archivo.write(texto)
    archivo.close()

#--------------------------------------INTERFAZ GRÁFICA--------------------------------------#
#VENTANA PRINCIPAL
main = Tk()
#main.maxsize(170 , 180)
main.title("Generador de Nombres al Azar")

#FONTS
labelFont = ("Helvetica" , 12)
resultadoFont = ("Helvetica" , 18)

#LABELS
labelRESULTADO = Label(main , text = "" , font = resultadoFont)
labelRESULTADO.grid(row = 2 , column = 0 , sticky = N+W+E , padx = 10 , pady = 2)

labelGRUPO = Label(main , text = "Grupo Actual:\n-" , font = labelFont)
labelGRUPO.grid(row = 0 , column = 0 , sticky = N+W+E , padx = 10 , pady = 2)

labelHISTORIAL = Label(main , text = "" , font = labelFont)
labelHISTORIAL.grid(row = 0 , rowspan = 3 , column = 1 , sticky = N+W+E+S , padx = 10 , pady = 2)

#BOTONES
buttonGENERAR = Button(main , text = "GENERAR" , width = 1 , height = 2 , command = generar)
buttonGENERAR.grid(row = 1 , column = 0 , sticky = W+E , padx = 10 , pady = 2)

#MENU#
menu = Menu(main)
main.config(menu = menu)

dropdownmenuArchivo = Menu(menu, tearoff=0)
menu.add_cascade(label = "Archivo" , menu = dropdownmenuArchivo)
dropdownmenuArchivo.add_command(label = "Cargar Grupo..." , command = cargar)
dropdownmenuArchivo.add_command(label = "Grupo Nuevo..." , command = crearGrupo)

dropdownmenuOpciones = Menu(menu, tearoff=0)
menu.add_cascade(label = "Opciones" , menu = dropdownmenuOpciones)
dropdownmenuOpciones.add_checkbutton(label = "Night Mode" , command = nightMode)
dropdownmenuOpciones.add_checkbutton(label = "Mostrar Historial" , command = mostrarHistorial)

#LOOP
main.mainloop()






















