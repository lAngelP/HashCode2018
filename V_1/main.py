import csv
from namedlist import namedlist

"""DATA STRUCTURES"""
Viaje = namedlist('Viaje', ['tIni', 'tFin', 'pIni', 'pFin', 'dist', 'numero'])
Coche = namedlist('Coche', ['step', 'position', 'viajes'])



def distancia(position1, position2):
    x1, y1 = position1
    x2, y2 = position2
    return abs(x2 - x1) + abs(y2 - y1)


"""INPUT"""


def output(rides, mode):
    with open("output/"+mode+".txt", 'w+') as out:
        i = 0
        for coche in rides:
            v = coche.viajes
            out.write(str(len(v)) + " " + " ".join([str(i) for i in v]) + "\n")
        out.close()

def create_coche():
    return Coche(step = 0, position = (0,0), viajes = [])

def input(MODE):
    with open('data/' + MODE + '.in') as f:
        input_reader = csv.reader(f, delimiter=' ')
        (ROWS, COLUMNS, VH, RIDES, BONUS, STEPS) = (int(x) for x in next(input_reader))

        def create_ride(source, i):
            (xIn, yIn, xFin, yFin, tIni, tFin) = (int(x) for x in next(source))
            return Viaje(tIni=tIni, tFin=tFin, pIni=(xIn, yIn), pFin=(xFin, yFin),
                         dist=distancia((xIn, yIn), (xFin, yFin)), numero=i)
        rides = [create_ride(input_reader, i) for i in range(RIDES)]

    return ROWS, COLUMNS, VH, RIDES, BONUS, STEPS, rides

def llega ( viaje, coche):
    dist = distancia(coche.position, viaje.pIni)
    return viaje.tFin >= viaje.dist + dist + coche.step


def add_viaje (coche, viaje, i, viaje_list, coche_steps):
        if llega(viaje, coche):
            coche.viajes.append(viaje.numero)
            coche.step += viaje.dist+distancia(coche.position, viaje.pIni)
            coche.position = viaje.pFin
            viaje_list.remove(viaje)
            coche_steps[i] = coche.step
            return
        else:
            viaje_list.remove(viaje)

def main(MODE):


    ROWS, COLUMNS, VH, RIDES, BONUS, STEPS, rides = input(MODE)
    coche_steps = [0]*VH
    coches = [None]*VH
    for i in range(VH):
        coches[i] = create_coche()
    ride_sorted = sorted(rides, key=lambda ride: ride.tIni)
    while ride_sorted:
        coche_distance = [distancia(ride_sorted[0].pIni, coche.position) for coche in coches]
        coche_distance = [x+y for x, y in zip(coche_distance, coche_steps)]
        coche_bonus = list(filter(lambda x: x == ride_sorted[0].tIni, coche_distance))
        coche_bonus = sorted(coche_bonus)
        if not coche_bonus:
            i = coche_distance.index(min(coche_distance))
        else:
            i = coche_distance.index(coche_bonus[0])
        if not ride_sorted:
            break
        add_viaje(coches[i], ride_sorted[0], i, ride_sorted, coche_steps)
        print(len(ride_sorted))
    output(coches, MODE)
    print(MODE)



if __name__ == "__main__":
    modes = ['a_example', 'b_should_be_easy', 'c_no_hurry', 'd_metropolis', 'e_high_bonus']
    for mode in modes:
        main(mode)


