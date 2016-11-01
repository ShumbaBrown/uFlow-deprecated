import math
import graph


def ConvertToCartesianGraph(points):
    # Accepts a list of points and return a list of (x, y)
    # values that represent the points on a cartesian graph

    noOfSpokes = len(points)
    angleOfSpokes = 360 / noOfSpokes
    listOfCartesianPoints = []
    
    theta = 0

    for point in points:
        # Calculate (x, y) Values
        sin = round(math.sin(math.radians(theta)))
        cos = round(math.cos(math.radians(theta)))
        x = (point * cos) - (0 * sin)
        y = (0 * cos) + (point * sin)
        cartesianPoint = [x, y]
        listOfCartesianPoints.append(cartesianPoint)
        theta += angleOfSpokes

    graph.graphPoints(listOfCartesianPoints)
    return listOfCartesianPoints

V = [100, 75, 50, 75]
ConvertToCartesianGraph(V)