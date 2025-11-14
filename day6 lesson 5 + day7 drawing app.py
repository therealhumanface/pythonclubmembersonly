import turtle
screen = turtle.Screen()
screen.title("I made a drawing app")
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.pensize(5)
t.pencolor("black")
def start_draw(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    screen.title("drawing")
def draw(x, y):
    t.ondrag(None)
    t.goto(x, y)
    t.ondrag(draw)
    screen.title("drawing")
def erase():
    t.clear()
    screen.title("erasing")
def red(): t.pencolor("red")
def blue():t.pencolor("blue")
def green():
    t.pencolor("green")
def black():
    t.pencolor("black")
def up():
    t.forward(10)
def down():
    t.backward(10)
def left():
    t.left(10)
def right(): t.right(10)
def savepic():
    canvas = screen.getcanvas()
    canvas.update()
    canvas.postscript(file="drawing.eps")
    from PIL import Image
    img = Image.open("drawing.eps")
t.ondrag(draw)
screen.onscreenclick(start_draw)
screen.onkey(erase, "space")
screen.onkey(red, "r")
screen.onkey(red, "R")
screen.onkey(blue, "b")
screen.onkey(blue, "B")
screen.onkey(green, "g")
screen.onkey(green, "G")
screen.onkey(black, "k")
screen.onkey(black, "K")
screen.onkey(savepic, "s")
screen.onkey(savepic, "S")
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()
screen.mainloop()