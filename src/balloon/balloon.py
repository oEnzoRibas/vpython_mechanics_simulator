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

ground = box(
    pos=vec(0, -30.5, 0), 
    size=vec(30, 0.2, 30), 
    texture=textures.granite
    )

# envelope = sphere(
#     pos=vec(0, 5, 0),
#     size=vec(4, 4.5, 4),
#     color=color.red,
# )

# outershape = [
#     [0.40, -0.40],
#     [0.40,  0.40],
#     [-0.40, 0.40],
#     [-0.40,-0.40],
#     [0.40,-0.40]
# ]

# innershape = [
#     [0.30,-0.30],
#     [0.30, 0.30],
#     [-0.30,0.30],
#     [-0.30,-0.30],
#     [0.30,-0.30]
# ]

# walls = extrusion(
#     shape=[outershape, innershape],
#     path=[
#         vec(0, 0.0, 0),
#         vec(0, .5, 0)
#     ],
#     color=vector(.55, .27, .07)
# )

# bottom = extrusion(
#     shape=outershape,
#     path=[
#         vec(0, 0.0, 0),
#         vec(0, 0.1, 0)
#     ],
#     color=vector(.55, .27, .07)
# )

# basket = compound([walls, bottom])

# ropes = []

# for sx in (-1, 1):
#     for sz in (-1, 1):

#         start = vec(sx * 0.30, 0.50, sz * 0.30)
#         end   = vec(sx * 0.75, 2.80, sz * 0.75)

#         ropes.append(
#             cylinder(
#                 pos=start,
#                 axis=end - start,
#                 radius=0.015,
#                 color=color.white
#             )
#         )

# balloon = compound([
#     envelope,
#     basket,
#     *ropes,
# ])

balloon = sphere(
    pos=vec(3, 0, 3), 
    size=vec(2, 2, 2),
    color=color.green
)

celular = box(
    pos=vec(0, 0, 3), 
    size=vec(2, 2, 2),
    color=color.red
)

t = 0
dt = 0.01

g_pos = graph(
    align="right",
    title="Ball Movement",
    xtitle="Time (s)",
    ytitle="Position",
    width=600,
    height=650,
    xmin=0,
    xmax=15,
    ymin=-10,
    ymax=20
)

g_pos_rel = graph(
    align="right",
    title="Relative Movement",
    xtitle="Time (s)",
    ytitle="Position",
    width=600,
    height=250,
    xmin=0,
    xmax=10,
    ymin=0,
    ymax=20
)

# g_vel = graph(
#     align="right",
#     title="Ball Movement",
#     xtitle="Time (s)",
#     ytitle="Position",
#     width=600,
#     height=250,
#     xmin=0,
#     xmax=10,
#     ymin=0,
#     ymax=20
# )

balloon_graph = gcurve(graph=g_pos, color=color.green)
celular_graph = gcurve(graph=g_pos, color=color.red)
cell_balloon = gcurve(graph=g_pos_rel, color= color.orange)

v0 = 4
v = v0
g = np.float64(-1)

while True:
    rate(60)

    if celular.pos.y <= -10:
        continue
    celular.pos.y = v0 * t + 0.5*g*t**2
# v = v + g * dt

    balloon.pos.y = v0*t



    celular_graph.plot(t, celular.pos.y)
    balloon_graph.plot(t, balloon.pos.y)
    cell_balloon.plot(t, balloon.pos.y-celular.pos.y)



    # if t > 10:
    #     g_pos.xmin = t - 10
    #     g_pos_rel.xmin = t - 10
    #     g_pos.xmax = t
    #     g_pos_rel.xmax = t

    t += dt