import turtle

def draw_square(t,sz):
    """Make turtle t draw a square of sz"""

    t.pendown()
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.penup()
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
t=turtle.Turtle()
t.color("HotPink")

for j in range(5):
    draw_square(t, 20 + 20 * j)

wn.mainloop()
