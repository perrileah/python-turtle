# t.rt() instead of t.right()
# t.fd() instead of t.forward()
# t.lt() instead of t.left()
# t.bk() instead of t.backward()

# Set up
import turtle
s = turtle.getscreen()
turtle.title("My First Turtle Program")
t = turtle.Turtle()
pen = turtle.Turtle()

# Background color
turtle.bgcolor("black")

# Move into position for pumpkin 
t.right(90)
t.forward(250)
t.left(90)

# Draw Pumpkin head 
t.fillcolor("orange")
t.begin_fill()
t.circle(280)
t.end_fill()

# Left Eye
pen.up()
pen.goto(-150, 100)
pen.down()
# Check position of pen 
pen.fillcolor("black")
pen.begin_fill()
# Position of pen 
pen.right(20)
pen.fd(100)
pen.lt(120)
pen.fd(100)
pen.lt(120)
pen.fd(100)
pen.end_fill()

# Right eye
pen.up()
pen.goto(150, 100)
pen.down()
# Pen position!
pen.right(60)
# Begin 
pen.fillcolor("black")
pen.begin_fill()
pen.fd(100)
pen.rt(120)
pen.fd(100)
pen.rt(120)
pen.fd(100)
pen.end_fill()

# Nose
pen.up()
pen.home()
pen.goto(50,0)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.lt(120)
pen.fd(70)
pen.lt(120)
pen.fd(70)
pen.lt(120)
pen.end_fill()

# Draw mouth - omg 
pen.goto(-150, -100)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.rt(50)
pen.fd(50)
pen.fd(20)
pen.lt(120)
pen.rt(20)
pen.fd(20)
pen.fd(50)
pen.rt(100)
pen.fd(70)
pen.lt(100)
pen.fd(70)
pen.rt(100)
pen.fd(70)
pen.lt(100)
pen.fd(70)
pen.fd(20)
pen.lt(50)
pen.lt(50)
pen.lt(20)
pen.lt(20)
pen.fd(50)
pen.rt(20)
pen.rt(10)
pen.rt(10)
pen.fd(50)
pen.fd(20)
pen.lt(100)
pen.rt(20)
pen.fd(50)
pen.rt(50)
pen.rt(20)
pen.rt(20)
pen.fd(50)
pen.fd(20)
pen.lt(50)
pen.lt(20)
pen.fd(50)
pen.undo()
pen.lt(10)
pen.lt(10)
pen.fd(50)
pen.rt(50)
pen.rt(20)
pen.rt(10)
pen.fd(50)
pen.fd(20)
pen.fd(10)
pen.lt(50)
pen.lt(50)
pen.lt(50)
pen.fd(20)
pen.undo()
pen.rt(10)
pen.fd(20)
pen.undo()
pen.rt(10)
pen.fd(20)
pen.lt(5)
pen.lt(5)
pen.lt(5)
pen.fd(10)
pen.fd(10)
pen.fd(10)
pen.undo()
pen.rt(10)
pen.fd(10)
pen.fd(5)
pen.end_fill()


# Stem
pen.up()
pen.goto(-20, 300)
pen.lt(70)
pen.down()
pen.fillcolor("green")
pen.begin_fill()
pen.fd(30)
pen.lt(90)
pen.fd(60)
pen.fd(20)
pen.lt(90)
pen.fd(60)
pen.lt(90)
pen.lt(10)
pen.rt(5)
pen.fd(60)
pen.fd(10)
pen.fd(10)
pen.end_fill()

