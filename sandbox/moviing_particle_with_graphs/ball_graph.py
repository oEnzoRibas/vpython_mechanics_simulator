from vpython import *
import numpy as np

scene = canvas(
    resizable=True,
    title="Balloon", 
    width=600, 
    height=600,
    align="left"
    )

trail_config = {
    "make_trail": True,
    "trail_type": "points",
    "trail_color": color.red,
    "trail_radius": .1
}

ball = sphere(
    pos=vector(0,0,0), 
    radius=2, 
    color=color.cyan,
    **trail_config
    )


grafico = graph(
    align="right",
    title="Ball Movement",
    xtitle="Time (s)",
    ytitle="Position",
    width=600,
    height=250,
    xmin=0,
    xmax=10
)

xmotion = gcurve(graph=grafico, color=color.red)
ymotion = gcurve(graph=grafico, color=color.blue)

t = 0.0
dt = 0.01

while True:
    rate(100)

    x = 9*np.sin(2*np.pi*t)*np.cos(2*np.pi*t)
    y = 4*np.sin(2*np.pi*t)

    ball.pos.x = x
    ball.pos.y = y

    xmotion.plot(t, x)
    ymotion.plot(t, y)

    if t > 10:
        grafico.xmin = t - 10
        grafico.xmax = t

    t += dt