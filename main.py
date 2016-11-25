from corredor import Corredor
from carrera import Carrera

nombre_corredor1 = input("Nombre del primer corredor: ")
nombre_corredor2 = input("Nombre del segundo corredor: ")

corredor1 = Corredor(nombre_corredor1)
corredor2 = Corredor(nombre_corredor2)

carrera = Carrera(corredor1, corredor2)

carrera.empieza()
carrera.termina()
