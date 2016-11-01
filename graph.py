import turtle

def graphPoints(coords):
    myTurtle = turtle.Turtle()
 

    theta = 360 / len(coords)
    myTurtle.seth(0)

    for i in range(len(coords)):
        myTurtle.goto(0, 0)
        myTurtle.seth(i * theta)
        myTurtle.begin_poly()
        myTurtle.fd(200)
        myTurtle.end_poly()

    myTurtle.penup()

    myTurtle.goto(coords[len(coords) - 1][0], coords[len(coords) - 1][1])
    myTurtle.pendown()

    for i in range(len(coords)):
        myTurtle.goto(coords[i][0], coords[i][1])
        


    myTurtle.penup()

    myTurtle.getscreen()._root.mainloop()
    '''
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
    '''
