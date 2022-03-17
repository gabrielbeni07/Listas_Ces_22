import turtle

def draw_poly(t, n, sz):
    """Make turtle t draw a regular polygon of n sides and side lenght sz"""
    
    for i in range(n):
        t.forward(sz)
        t.left(360/n)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
t=turtle.Turtle()
t.color("HotPink")
draw_poly(t, 3, 100)
wn.mainloop()