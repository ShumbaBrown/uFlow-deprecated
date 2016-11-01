import turtle

def graphPoints(coords):
    myTurtle = turtle.Turtle()
    myTurtle.begin_poly()
    myTurtle.goto(0, 120)
    myTurtle.goto(0, -120)
    myTurtle.home()
    myTurtle.goto(120, 0)
    myTurtle.goto(-120, 0)
    myTurtle.end_poly()
    myTurtle.begin_poly()

    for coord in coords:
        myTurtle.goto(coord[0], coord[1])
    myTurtle.goto(coords[0][0], coords[0][1])
    myTurtle.end_poly()
    myTurtle.getscreen()._root.mainloop()
