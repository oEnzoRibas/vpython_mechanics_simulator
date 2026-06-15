from vpython import *
import numpy as np

def main():
    #canvas(
    #    title="Free Fall",
    #    width=1920,
    #    height=1080
    #)

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

    dt = np.float64(0.01)
    v = np.float64(0)
    g = np.float64(909.78)


    while True:
        rate(60)

        v += -g * dt
        ball.pos.y += v * dt

        ball_edge = ball.pos.y - ball.radius
        floor_top_surface = floor.pos.y + floor.size.y/2

        if ball_edge <= floor_top_surface:
            #penetration = floor_top_surface - ball_edge
            #ball.pos.y = floor_top_surface + ball.radius + penetration
            
            ball.pos.y = floor_top_surface + ball.radius
            v = -v


if __name__ == "__main__":
    main()
