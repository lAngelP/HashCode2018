import csv
from namedlist import namedlist

MODE = "a_example"

"""DATA STRUCTURES"""
Viaje = namedlist('Viaje', ['tIni', 'tFin', 'pIni', 'pFin', 'dist'])
Coche = namedlist('Coche', ['step', 'position', 'viajes'])

def da_tiempo (coche, viaje):
    if viaje.duration+coche.step+ distancia(coche.position, viaje.pFin) > viaje.tFin:
        return False, 0, 0
    else:
        return True, viaje.duration, distancia(coche.position, viaje.pFin)

def distancia(position1, position2):
    x1, y1 = position1
    x2, y2 = position2
    return abs(x2 - x1) + abs(y2 - y1)

"""INPUT"""
def input(MODE):
    with open('HashCode2018/data/'+MODE+'.in') as f:
        input_reader = csv.reader(f, delimiter=' ')
        (ROWS, COLUMNS, VH, RIDES, BONUS, STEPS) = (int(x) for x in next(input_reader))

        def create_ride(source):
            (xIn, yIn, xFin, yFin, tIni, tFin) = (int(x) for x in next(source))
            return Viaje(tIni=tIni, tFin=tFin, pIni=(xIn, yIn), pFin=(xFin, yFin),
                    dist=distancia((xIn, yIn), (xFin, yFin)))

        rides = [create_ride(input_reader) for _ in range(RIDES)]

    return ROWS, COLUMNS, VH, RIDES, BONUS, STEPS, rides

print(input(MODE))
