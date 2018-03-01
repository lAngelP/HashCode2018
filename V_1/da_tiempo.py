
def distancia(position1, position2):
    x1, y1 = position1
    x2, y2 = position2
    return abs(x2 - x1) + abs(y2 - y1)

def da_tiempo (coche, viaje):
    if viaje.duration+coche.step+ distancia(coche.position, viaje.final) > viaje.tiempo_final:
        return False, 0, 0
    else:
        return True, viaje.duration, distancia(coche.position, viaje.final)