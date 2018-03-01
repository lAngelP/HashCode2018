import csv
from namedlist import namedlist

MODE = "a_example"

"""DATA STRUCTURES"""
Ride = namedlist('Ride', ['tIni', 'tFin', 'pIni', 'pFin', 'dist'])
Coche = namedlist('Coche', ['step', 'pActual', 'viajes'])

def input(MODE):
    with open('data/'+MODE+'.in') as f:
        input_reader = csv.reader(f, delimiter=' ')
        (ROWS, COLUMNS, VH, RIDES, BONUS, STEPS) = (int(x) for x in next(input_reader))

        def create_ride(source):
            (xIn, yIn, xFin, yFin, tIni, tFin) = (int(x) for x in next(source))
            return Ride(tIni=tIni, tFin=tFin, pIni=(xIn, yIn), pFin=(xFin, yFin))

        rides = [ for line in input_reader]

    return ROWS, COLUMNS, VH, RIDES, BONUS, STEPS, rides

"""OUTPUT"""
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
