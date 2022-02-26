import math
import random
import tablero
import reglas
import datetime
#print(int(datetime.datetime.timestamp(datetime.datetime.now())))
#print(time.microsecond)
random.seed(int(datetime.datetime.timestamp(datetime.datetime.now())))
#random.seed(5) 

jugadores=[]
numeroJugadores=tablero.numero("Pulse el 1 para jugar con la computadora y 0 para salir: " ,0,2)
for i in range(numeroJugadores):
   jugadores.append({"nombre":input("Escriba su nombre: "),"tipo":"H"})
for i in range(2-numeroJugadores):
   jugadores.append({"nombre":"Computadora ","tipo":"M"})

for jugador in jugadores:
   print("\t",jugador["nombre"])
numeroPartidas=1
if(numeroJugadores>0):
   empieza=tablero.numero("¿Que jugador Ataca? \n Presione 1 para atacar o 2 para que la computadora inicie: ",1,2)
   if(empieza==2):
      jugadores.reverse()
else:
   numeroPartidas=tablero.numero("Número de partidas a jugas [0-500]: ",0,500)
logJugada=""
resultados={"Ganadas":0,"Perdidas":0,"Empatadas":0}
for jugada in range(numeroPartidas):
   #Iniciamos el juego
   #if len(logJugada)>0:
   #   print(logJugada)
   logJugada=""
   tablero.inicializar()
   continuar=True
   fichasEnTablero=0
   while continuar:
      #Pedimos posición de la ficha
      if(numeroJugadores!=0):
         tablero.pintarTablero()
      numJugador=(fichasEnTablero&1)
      ficha='X' if numJugador==1 else 'O'
      logJugada+="Juega "+ficha+" - "
      if(jugadores[numJugador]["tipo"]=="H"):
         casilla=reglas.colocarFicha(ficha)
      else:
         casilla=reglas.colocarFichaMaquina(ficha,'X' if numJugador==0 else 'O',tablero.tablero)
      if casilla==-1:
         tablero.pintarTablero()
         continuar=False
         continue
      logJugada+="casilla "+str(casilla)+" - "
      tablero.casillasVacias.remove(casilla)
      if(reglas.hemosGanado(casilla,ficha,tablero.tablero)):
         continuar=False
         if numeroJugadores>0:
            print(jugadores[numJugador]["nombre"],"¡¡¡¡¡Has ganado!!!!")
         else:
            logJugada+="Ha ganado "+jugadores[numJugador]["nombre"]+"\n"
         if(numJugador==0):
            resultados["Ganadas"]=resultados["Ganadas"]+1
         else:
            resultados["Perdidas"]=resultados["Perdidas"]+1
      fichasEnTablero+=1
      if(fichasEnTablero==9 and continuar):
         continuar=False
         resultados["Empatadas"]=resultados["Empatadas"]+1
         if numeroJugadores>0:
            print("TABLAS")
         else:
            logJugada+="Ha quedado en tablas \n"
   if numeroJugadores>0:
      tablero.pintarTablero()
print(resultados)