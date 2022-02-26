import math
import random
import tablero
import estrategia1
import estrategia2
NIVEL_DESPISTE=-1
#Colaca una ficha en el tablero

def numeroHermanos(casilla, ficha, v, h,tablero):
   f=math.floor(casilla/tablero.TABLERO_COLUMNAS) #Obtengo la fila
   c=casilla % tablero.TABLERO_COLUMNAS #columna
   fila_nueva=f+v
   if(fila_nueva<0 or fila_nueva>=tablero.TABLERO_FILAS):
      return 0
   columna_nueva=c+h
   if(columna_nueva<0 or columna_nueva>=tablero.TABLERO_COLUMNAS):
      return 0
   #No estamos en el limite así que
   #calculamos la nueva posición y vemos si hay la misma ficha
   pos=(fila_nueva*tablero.TABLERO_COLUMNAS+columna_nueva)
   if(tablero[pos]!=ficha):
      return 0
   else:
      return 1+numeroHermanos(pos,ficha,v,h,tablero)

# comprobamos que la ficha colocada en la casilla indica tiene dos fichas similares en casillas contiguas
def hemosGanado(casilla, ficha, tablero):
   hermanos=numeroHermanos(casilla,ficha,-1,-1,tablero)+numeroHermanos(casilla,ficha,1,1,tablero)
   if(hermanos==2):
      return True
   hermanos=numeroHermanos(casilla,ficha,1,-1,tablero)+numeroHermanos(casilla,ficha,-1,1,tablero)
   if(hermanos==2):
      return True
   hermanos=numeroHermanos(casilla,ficha,-1,0,tablero)+numeroHermanos(casilla,ficha,1,0,tablero)
   if(hermanos==2):
      return True
   hermanos=numeroHermanos(casilla,ficha,0,-1,tablero)+numeroHermanos(casilla,ficha,0,1,tablero)
   if(hermanos==2):
      return True

def colocarFicha(ficha):
   print("Marca una posición que no esté ocupada")
   while True:
      fila=tablero.numero("La fila esta entre 1 y 3: ", 1,3)-1 #Restamos uno ya que nuestro rango real está entre 0 y 2
      columna=tablero.numero("La fila esta entre 1 y 3:  ",1,3)-1
      #Como mi tablero es de 3x3
      casilla=fila*tablero.TABLERO_COLUMNAS+columna
      if(tablero.tablero[casilla]!=' '):
         #Esa casilla ya está cubierta
         print("La casilla está ocupada")
      else:
         tablero.tablero[casilla]=ficha
         return casilla
def colocarFichaMaquina(ficha, fichaContrincante, tablero):
   random.shuffle(tablero.casillasVacias)
   despiste=random.randint(0,100)
   
   
   for casilla in tablero.casillasVacias:
      if(hemosGanado(casilla,ficha, tablero)):
         if(despiste>NIVEL_DESPISTE):
            tablero.tablero[casilla]=ficha
            return casilla
         else:
            print("No nos hemos fijado en que podíamos ganar")
   despiste=random.randint(0,100)
   for casilla in tablero.casillasVacias:
      if(hemosGanado(casilla,fichaContrincante, tablero)):
         if(despiste>NIVEL_DESPISTE):
            tablero.tablero[casilla]=ficha
            return casilla
         else:
            print("No nos hemos dado cuenta de que nos podían ganar")
   if ficha =="X":
      mejorOpcion=estrategia2.laOpcion(tablero,tablero.casillasVacias,ficha,False)
   else:
      mejorOpcion=estrategia1.laOpcion(tablero,tablero.casillasVacias,ficha,False)

   if(mejorOpcion!=-1):
      casilla=mejorOpcion
   else:
      if(len(tablero.casillasVacias)>0):
         print("No hay mejor opción así que escojemos la primera de todas")
         casilla=tablero.casillasVacias[0]
      else:
         return -1
   tablero.tablero[casilla]=ficha
   return casilla


