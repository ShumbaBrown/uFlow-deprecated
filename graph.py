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
