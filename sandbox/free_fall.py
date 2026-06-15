from vpython import *
import numpy as np
import csv

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
    g = np.float64(-10)

    t =0
    xi = 0


    with open("saida.csv", "w", encoding="utf-8",) as file:
        writer = csv.writer(file)
        writer.writerow(["tempo_dt", "posicao_y", "xi", "velocidade_v", "aceleracao"])

        while True:
            rate(60)
            t += dt - 0.01

            file.write(f"{t}, {ball.pos.y}, {xi}, {v}, {g}\n")

            v = v + g * dt
            ball.pos.y = ball.pos.y + v * dt + 0.5*g*dt**2

            xi = ball.pos.y + v*dt

            ball_edge = ball.pos.y - ball.radius
            floor_top_surface = floor.pos.y + floor.size.y/2

            if ball_edge <= floor_top_surface:
                ball.pos.y = floor_top_surface + ball.radius
                v = -v

if __name__ == "__main__":
    main()
