from vpython import *

ball = sphere(
    pos=vector(0,10,0),
    radius=1,
    color=color.red
)

floor = box(
    pos=vector(0,-10,0),
    size=vector(10,0.5,10),
    color=color.green
)

dt = 0.01
v = 0
g = 9.78

while True:
    rate(60)

    v -= g*dt
    ball.pos.y += v * dt

    if (ball.pos.y - ball.radius) <= floor.pos.y:
        v = -v