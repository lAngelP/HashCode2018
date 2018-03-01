import csv
from namedlist import namedlist

MODE = "b_should_be_easy"

#DATA STRUCTURES
Viaje = namedlist('Ride', ['tIni', 'tFin', 'pIni', 'pFin', 'dist'])
Coche = namedlist('Coche', ['step', 'pActual', 'viajes'])

def da_tiempo (coche, viaje):
    if viaje.duration+coche.step+ distancia(coche.position, viaje.pFin) > viaje.tFin:
        return False, 0, 0
    else:
        return True, viaje.duration, distancia(coche.position, viaje.pFin)

def distancia(position1, position2):
    x1, y1 = position1
    x2, y2 = position2
    return abs(x2 - x1) + abs(y2 - y1)

#INPUT
def input(MODE):
    with open('data/'+MODE+'.in') as f:
        input_reader = csv.reader(f, delimiter=' ')
        (ROWS, COLUMNS, VH, RIDES, BONUS, STEPS) = (int(x) for x in next(input_reader))

        def create_ride(source):
            (xIn, yIn, xFin, yFin, tIni, tFin) = (int(x) for x in next(source))
            return Viaje(tIni=tIni, tFin=tFin, pIni=(xIn, yIn), pFin=(xFin, yFin),
                    dist=distancia((xIn, yIn), (xFin, yFin)))

        rides = [create_ride(input_reader) for _ in range(RIDES)]

    return ROWS, COLUMNS, VH, RIDES, BONUS, STEPS, rides


#OUTPUT
def output(rides):
    with open("s_p.txt", 'w+') as out:
        i = 0
        for coche in rides:
            v = coche.viajes
            i += 1
            out.write(str(i)+" "+" ".join([str(i) for i in v])+"\n")
        out.close()
        print(i)

print(input(MODE))
