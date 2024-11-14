""" You are given four tuples. In each tuple there is coordinates x and y of a point. There is one and only one line, that goes through two points, so with four points you can have two lines: first and second tuple is two points of a first line, thirs and fourth tuple is two points of the second line. Your task is to find and return a tuple with x and y coordinates of lines crossing point.

Numbers can be positive as well as negative, integer or floats. Your answer shouldn't be rounded!!

Note, that if two lines are the same ( have infinite crossing points ) or parallel ( have no crossing points ), you will need to return None/Nothing depending on language. """


def find_the_crossing(a, b, c, d):
    # extraer coordenadas
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    x3, y3 = c[0], c[1]
    x4, y4 = d[0], d[1]

    # calcular pendientes de las rectas
    m1 = (y2 - y1) / (x2 - x1)
    m2 = (y4 - y3) / (x4 - x3)

    # calculo del intercepto
    b1 = y1 - m1 * x1
    b2 = y3 - m2 * x3

    # comprobacion de lineas paralelas
    if m1 == m2:
        return None

    # ambas lineas son coincidentes y tienen infinitos puntos de interseccion
    if m1 == m2:
        if b1 == b2:
            return None
        return None

    # calculo del punto de interseccion
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1

    return (x, y)
