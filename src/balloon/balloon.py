from vpython import *
import numpy as np

trail_config = {
    "make_trail": True,
    "trail_type": "points",
    "trail_color": color.red,
    "trail_radius": .1
}

scene = canvas(
    align="left",
    width=600,
    height=600,
    background=vector(0.53, 0.81, 0.98),
    title="Gas Balloon"
)

scene.center = vec(0, 4, 0)
scene.range = 10

ground = sphere(
    pos=vec(0, -10.5, 0), 
    size=vec(30, 0.2, 30), 
    texture=textures.earth
    )

envelope = sphere(
    pos=vec(0, 5, 0),
    size=vec(4, 4.5, 4),
    color=color.red,
)

outershape = [
    [0.40, -0.40],
    [0.40,  0.40],
    [-0.40, 0.40],
    [-0.40,-0.40],
    [0.40,-0.40]
]

innershape = [
    [0.30,-0.30],
    [0.30, 0.30],
    [-0.30,0.30],
    [-0.30,-0.30],
    [0.30,-0.30]
]

walls = extrusion(
    shape=[outershape, innershape],
    path=[
        vec(0, 0.0, 0),
        vec(0, .5, 0)
    ],
    color=vector(.55, .27, .07)
)

bottom = extrusion(
    shape=outershape,
    path=[
        vec(0, 0.0, 0),
        vec(0, 0.1, 0)
    ],
    color=vector(.55, .27, .07)
)

basket = compound([walls, bottom])

ropes = []

for sx in (-1, 1):
    for sz in (-1, 1):

        start = vec(sx * 0.30, 0.50, sz * 0.30)
        end   = vec(sx * 0.75, 2.80, sz * 0.75)

        ropes.append(
            cylinder(
                pos=start,
                axis=end - start,
                radius=0.015,
                color=color.white
            )
        )

balloon = compound([
    envelope,
    basket,
    *ropes,
])

balloon.pos = vec(0, 0, 0)

t = 0
dt = 0.01


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
zmotion = gcurve(graph=grafico, color=vector(0.5,1,.3))

while True:
    rate(100)

    x = 9 * np.sin(2*np.pi*t) + 10*np.e**(-0.5*t)*np.cos(2*np.pi*t)
    y = 9 * np.cos(2*np.pi*t)* 3*np.e**(-0.5*t)
    z  = 10*np.e**(-0.1*t) * np.sin(t)

    balloon.pos = vec(x, y, z)

    xmotion.plot(t, x)
    ymotion.plot(t, y)
    zmotion.plot(t, z)

    if t > 10:
        grafico.xmin = t - 10
        grafico.xmax = t

    t += dt