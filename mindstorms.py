import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create the turtle Brad - Draw a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

#def draw_shapes():
#    window = turtle.Screen()
#    window.bgcolor("red")
    
#    brad = turtle.Turtle()
#    brad.shape("turtle")
#    brad.color("blue", "green")
#    brad.speed(1)
    
#    times_run = 0

#    while (times_run < 4):
#        brad.forward(100)
#        brad.right(90)
#        times_run = times_run + 1

#    angie = turtle.Turtle()
#    angie.shape("arrow")
#    angie.color("yellow")
#    angie.circle(100)

#    christine = turtle.Turtle()
#    christine.shape("circle")
#    christine.color("white")

#    christine_i = 0

#    while (christine_i < 3):
#        christine.forward(100)
#        christine.left(120)
#        christine_i = christine_i + 1

#    window.exitonclick()


draw_art()
