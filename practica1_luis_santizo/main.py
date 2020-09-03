import json
import numpy as np
import webbrowser
import re
menor=[0]
nombre=[]
edad=[]
activo =[]
promedio=[]
atributos =["nombre","edad","activo","promedio"]
archivo=[]
carga_archivos = []

def cargar(archivo):
  for i in archivo:

      with open(i+".json") as ruta:
          info=json.loads(ruta.read())
          carga_archivos.append(info)
          print("archivo__"+i+"_____carga completa")
  timer =0
  for a in carga_archivos:
      for b in range(len(a)):
          nombre.append(carga_archivos[timer][b]["nombre"])
          edad.append(carga_archivos[timer][b]["edad"])
          promedio.append((carga_archivos[timer][b]["promedio"]))
          activo.append((carga_archivos[timer][b]["activo"]))

      timer +=1











def main():


    print("ingrese ruta")
    ingresar=input().split(",")
    archivo = ingresar
    comand = ingresar[0][:6]
    archivo[0] = archivo[0].replace(" ","")
    archivo[0] = archivo[0][6:]
    if(comand.lower()=="cargar"):
        for a in range(len(archivo)):
            archivo[a]= archivo[a].replace(" ","")
    cargar(archivo)
    menu()

def menu():
    print("menu")
    opciones = input()
    while opciones != "salir":
        if opciones == "seleccionar":
            siguiente()
        if opciones == "maximo":
            maximos()
        if opciones == "minimo":
            minimo()
        if opciones == "suma":
            sedades()
        if opciones == "cuenta":
            scuentas()
        if opciones == "reporte":
            reporte()



def siguiente():

    opcion1 =input()
    opcion2 = input()
    opcion3 = input()
    opcion4 = input()
    opcion5 = input()
   #-------------------------------NOMBRE[0][0]-----------------------
    if(opcion1==carga_archivos[0][0]["nombre"]):
        if(opcion2 == "nombre"):
            print(carga_archivos[0][0]["nombre"])
        if(opcion3 =="edad"):
            print(carga_archivos[0][0]["edad"])
        if(opcion4=="promedio"):
            print(carga_archivos[0][0]["promedio"])
        if(opcion5=="activo"):
            print(carga_archivos[0][0]["activo"])
    #------------------------------EDAD[0][0]-----------------------
    a =str(carga_archivos[0][0]["edad"])
    if (opcion1 ==a):
        if (opcion2 == "nombre"):
            print(carga_archivos[0][0]["nombre"])
        if (opcion3 == "edad"):
            print(carga_archivos[0][0]["edad"])
        if (opcion4 == "promedio"):
            print(carga_archivos[0][0]["promedio"])
        if (opcion5 == "activo"):
            print(carga_archivos[0][0]["activo"])
 #------------------------------PROMEDIO[0][0]-----------------------
    b =str(carga_archivos[0][0]["promedio"])
    if (opcion1 ==b):
        if (opcion2 == "nombre"):
            print(carga_archivos[0][0]["nombre"])
        if (opcion3 == "edad"):
            print(carga_archivos[0][0]["edad"])
        if (opcion4 == "promedio"):
            print(carga_archivos[0][0]["promedio"])
        if (opcion5 == "activo"):
            print(carga_archivos[0][0]["activo"])
#-------------------------------ACTIVO[0][0]-----------------------------------------------------
    c =str(carga_archivos[0][0]["activo"])
    if (opcion1 ==c):
        if (opcion2 == "nombre"):
            print(carga_archivos[0][0]["nombre"])
        if (opcion3 == "edad"):
            print(carga_archivos[0][0]["edad"])
        if (opcion4 == "promedio"):
            print(carga_archivos[0][0]["promedio"])
        if (opcion5 == "activo"):
            print(carga_archivos[0][0]["activo"])

#---------------------------------------------------------------------------------------------------------------------------------------------
 #-------------------------------NOMBRE[0][1]-----------------------
    if(opcion1==carga_archivos[0][1]["nombre"]):
        if(opcion2 == "nombre"):
            print(carga_archivos[0][1]["nombre"])
        if(opcion3 =="edad"):
            print(carga_archivos[0][1]["edad"])
        if(opcion4=="promedio"):
            print(carga_archivos[0][1]["promedio"])
        if(opcion5=="activo"):
            print(carga_archivos[0][1]["activo"])
    #------------------------------EDAD[0][1]-----------------------
    d =str(carga_archivos[0][1]["edad"])
    if (opcion1 ==d):
        if (opcion2 == "nombre"):
            print(carga_archivos[0][1]["nombre"])
        if (opcion3 == "edad"):
            print(carga_archivos[0][1]["edad"])
        if (opcion4 == "promedio"):
            print(carga_archivos[0][1]["promedio"])
        if (opcion5 == "activo"):
            print(carga_archivos[0][1]["activo"])
 #------------------------------PROMEDIO[0][1]-----------------------
    e =str(carga_archivos[0][1]["promedio"])
    if (opcion1 ==e):
        if (opcion2 == "nombre"):
            print(carga_archivos[0][1]["nombre"])
        if (opcion3 == "edad"):
            print(carga_archivos[0][1]["edad"])
        if (opcion4 == "promedio"):
            print(carga_archivos[0][1]["promedio"])
        if (opcion5 == "activo"):
            print(carga_archivos[0][1]["activo"])
#-------------------------------ACTIVO[0][1]-----------------------------------------------------
    f =str(carga_archivos[0][1]["activo"])
    if (opcion1 ==f):
        if (opcion2 == "nombre"):
            print(carga_archivos[0][1]["nombre"])
        if (opcion3 == "edad"):
            print(carga_archivos[0][1]["edad"])
        if (opcion4 == "promedio"):
            print(carga_archivos[0][1]["promedio"])
        if (opcion5 == "activo"):
            print(carga_archivos[0][1]["activo"])
   #-------------------------------NOMBRE[1][0]-----------------------
    if(opcion1==carga_archivos[1][0]["nombre"]):
        if(opcion2 == "nombre"):
            print(carga_archivos[1][0]["nombre"])
        if(opcion3 =="edad"):
            print(carga_archivos[1][0]["edad"])
        if(opcion4=="promedio"):
            print(carga_archivos[1][0]["promedio"])
        if(opcion5=="activo"):
            print(carga_archivos[1][0]["activo"])
    #------------------------------EDAD[1][0]-----------------------
    g =str(carga_archivos[1][0]["edad"])
    if (opcion1 ==g):
        if (opcion2 == "nombre"):
            print(carga_archivos[1][0]["nombre"])
        if (opcion3 == "edad"):
            print(carga_archivos[1][0]["edad"])
        if (opcion4 == "promedio"):
            print(carga_archivos[1][0]["promedio"])
        if (opcion5 == "activo"):
            print(carga_archivos[1][0]["activo"])
 #------------------------------PROMEDIO[1][0]-----------------------
    h =str(carga_archivos[1][0]["promedio"])
    if (opcion1 ==h):
        if (opcion2 == "nombre"):
            print(carga_archivos[1][0]["nombre"])
        if (opcion3 == "edad"):
            print(carga_archivos[1][0]["edad"])
        if (opcion4 == "promedio"):
            print(carga_archivos[1][0]["promedio"])
        if (opcion5 == "activo"):
            print(carga_archivos[1][0]["activo"])
#-------------------------------ACTIVO[1][0]-----------------------------------------------------
    i =str(carga_archivos[1][0]["activo"])
    if (opcion1 ==i):
        if (opcion2 == "nombre"):
            print(carga_archivos[1][0]["nombre"])
        if (opcion3 == "edad"):
            print(carga_archivos[1][0]["edad"])
        if (opcion4 == "promedio"):
            print(carga_archivos[1][0]["promedio"])
        if (opcion5 == "activo"):
            print(carga_archivos[1][0]["activo"])

#---------------------------------------------------------------------------------------------------------------------------------------------
 #-------------------------------NOMBRE[1][1]-----------------------
    if(opcion1==carga_archivos[1][1]["nombre"]):
        if(opcion2 == "nombre"):
            print(carga_archivos[1][1]["nombre"])
        if(opcion3 =="edad"):
            print(carga_archivos[1][1]["edad"])
        if(opcion4=="promedio"):
            print(carga_archivos[1][1]["promedio"])
        if(opcion5=="activo"):
            print(carga_archivos[1][1]["activo"])
    #------------------------------EDAD[1][1]-----------------------
    j =str(carga_archivos[1][1]["edad"])
    if (opcion1 ==j):
        if (opcion2 == "nombre"):
            print(carga_archivos[1][1]["nombre"])
        if (opcion3 == "edad"):
            print(carga_archivos[1][1]["edad"])
        if (opcion4 == "promedio"):
            print(carga_archivos[1][1]["promedio"])
        if (opcion5 == "activo"):
            print(carga_archivos[1][1]["activo"])
 #------------------------------PROMEDIO[1][1]-----------------------
    k =str(carga_archivos[1][1]["promedio"])
    if (opcion1 ==k):
        if (opcion2 == "nombre"):
            print(carga_archivos[1][1]["nombre"])
        if (opcion3 == "edad"):
            print(carga_archivos[1][1]["edad"])
        if (opcion4 == "promedio"):
            print(carga_archivos[1][1]["promedio"])
        if (opcion5 == "activo"):
            print(carga_archivos[1][1]["activo"])
#-------------------------------ACTIVO[1][1]-----------------------------------------------------
    l =str(carga_archivos[1][1]["activo"])
    if (opcion1 ==l):
        if (opcion2 == "nombre"):
            print(carga_archivos[1][1]["nombre"])
        if (opcion3 == "edad"):
            print(carga_archivos[1][1]["edad"])
        if (opcion4 == "promedio"):
            print(carga_archivos[1][1]["promedio"])
        if (opcion5 == "activo"):
            print(carga_archivos[1][1]["activo"])

    menu()


def maximos():
   print("entro")
   maxE =input()
   if(maxE=="maximo edad"):
       maximiso = np.array(edad)
       print("Edad maxima es >>>>>>"+str(np.amax(maximiso)))
   maxD = input()
   if (maxD == "maximo promedio"):
       maximiso = np.array(promedio)
       print("promedio maxima es >>>>>>" + str(np.amax(maximiso)))
   menu()

def minimo():
    print("entro")
    maxE = input()
    if (maxE == "minimo edad"):
        maximiso = np.array(edad)
        print("Edad minima es >>>>>>" + str(np.amin(maximiso)))
    maxD = input()
    if (maxD == "minimo promedio"):
        maximiso = np.array(promedio)
        print("promedio minimo es >>>>>>" + str(np.amin(maximiso)))
    menu()


def sedades():
    print("entro")
    ayuda = input()
    if ayuda == "suma edad":
        edades(edad)
    spromedio()

def spromedio():
    ayuda = input()
    if ayuda == "suma promedio":
        promedios(promedio)
    menu()

def scuentas():
    ayuda = input()
    if ayuda =="cuenta":
        print("numero de registro>>"+str(len(nombre)))
    menu()

def reporte():
    #' ' \

  numero1 = input()
  numero =int(numero1)

  css = '<!DOCTYPE html> \n <html lang = "en"> \n <head> \n <meta charset = "utf-8">\n<title>Reporte</title>\n' + '<link rel="stylesheet"  href="estilo.css">\n'
  css = css + '</head>\n<body>\n<center>\n<table border ="1">\n<tr> '
  for element in range(len(atributos)):
      nmbs = '<th bgcolor="blue">'+atributos[element]+'</th>'
      css =css + nmbs

  for element2 in range(numero):
      ayuda = '<tr> \n <td>'+ str(nombre[element2]) +'</td> <td>'+ str(edad[element2]) +'</td> <td>'+str(promedio[element2])+'</td> <td>'+str(activo[element2])+'</td>'
      ayuda = ayuda + '\n</tr>\n '
      css = css+ayuda
  css = css +'</table> \n </center> \n </body>\n </html> '
  crate = open("reporetes.html","w")
  crate.write(css)
  crate.close()
  webbrowser.open_new_tab("reporetes.html")
  menu()

#__________________________________FUNCIONES_________________________--

def edades(numerosSumas):
    sumaE =0
    for a in numerosSumas:
        sumaE=sumaE+a
    print("suma edades es de>>>>>"+str(sumaE))

def promedios(promediosSumas):
    sumaP =0
    for a in promediosSumas:
        sumaP = sumaP+a
    print("suma promedios>>>>>"+str(sumaP))


main()

