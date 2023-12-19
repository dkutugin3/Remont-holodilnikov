import matplotlib as mpl
import matplotlib.pyplot as plt
from itertools import count
import math


def launch():
    # начальные параметры
    m1 = 5.2915 * 10 ** 22
    m2 = 282253
    ship_pos = (0, 6 * 10 ** 5)
    modforce = 4 * 10 ** 6
    mass_decr = 259 * 4
    v = (0, 0)
    phi = 0

    # параметр дифферинцирования
    dt = 0.005

    fig, ax = plt.subplots()

    xs = []
    ys = []

    for p in count(0, 0.005):
        if p > 2 * math.pi:
            break

        xs.append(6 * 10 ** 5 * math.cos(p))
        ys.append(6 * 10 ** 5 * math.sin(p))

    ax.plot(xs, ys, label='ellipse')

    xs = []
    ys = []
    maxlen = 0
    maxv = 0

    with open("data/launch_mod.txt", 'w', encoding="UTF-8") as file:
        for t in count(0, dt):
            if 117.8 < t:
                if (v[0] ** 2 + v[1] ** 2) ** 0.5 > 2206:
                    mass_decr = 0
                    modforce = 0
                elif (ship_pos[0] ** 2 + ship_pos[1] ** 2) ** 0.5 > 700000:
                    mass_decr = 259 * 4
                    modforce = 4 * 10 ** 6
                    phi = math.pi / 2 + 0.02
                else:
                    mass_decr = 0
                    modforce = 0
            if t > 2500:
                break

            xs.append(ship_pos[0])
            ys.append(ship_pos[1])

            if t < 350:
                if t % 0.5 < dt:
                    file.write(f"{t:.2f} {(v[0] ** 2 + v[1] ** 2) ** 0.5:.2f}\n")

            modmg = 6.67 * (10 ** -11) * m1 * m2 / (ship_pos[0] ** 2 + ship_pos[1] ** 2)
            length = (ship_pos[0] ** 2 + ship_pos[1] ** 2) ** 0.5
            maxlen = max(maxlen, length)
            mg = (-ship_pos[0] / length * modmg, -ship_pos[1] / length * modmg)
            phi = max(phi, min(((length - 6 * 10 ** 5) / (4 * 10 ** 4)) ** 1.5, 1.0) * (math.pi / 4))
            try:
                teta = math.atan2(-mg[1], -mg[0])
            except ZeroDivisionError:
                teta = math.pi / 2

            force = (modforce * math.cos(teta - phi), modforce * math.sin(teta - phi))

            accel = ((mg[0] + force[0]) / m2, (mg[1] + force[1]) / m2)
            v = (v[0] + accel[0] * dt, v[1] + accel[1] * dt)
            maxv = max(maxv, (v[0] ** 2 + v[1] ** 2) ** 0.5)

            ship_pos = (ship_pos[0] + v[0] * dt, ship_pos[1] + v[1] * dt)

            m2 = m2 - mass_decr * dt

    ax.plot(xs, ys)
    print(f"Апоцентр: {maxlen - 6 * 10 ** 5}\nМакс скорость: {maxv}\nОстаток топлива: {m2 - 64000}")
    plt.show()


def trans():
    # начальные параметры
    a = (1.36 + 0.9832) / 2 * 10 ** 10
    c = a - 0.9832 * 10 ** 10
    e = c / a
    b = (a ** 2 - e ** 2) ** 0.5
    m1 = 1.7565 * 10 ** 28
    v = (0, 8505.8)

    modv = (v[0] ** 2 + v[1] ** 2) ** 0.5
    sun_pos = (-c, 0)
    ship_pos = (a, 0)

    # параметр дифферинцирования
    dt = 0.2

    fig2, ax2 = plt.subplots()

    xs = []
    ys = []

    for p in count(0, 0.005):
        if p > 2 * math.pi:
            break

        xs.append(a * math.cos(p))
        ys.append(b * math.sin(p))

    ax2.plot(xs, ys, label='ellipse')

    xs = []
    ys = []
    with open("data/obt_tr_mod.txt", 'w', encoding="UTF-8") as file:
        for t in count(0, dt):
            if ship_pos[1] < 0:
                file.write(f'{t / 3600:.2f} {modv:.2f}\n')
                break
            if t % 3600 < dt:
                xs.append(ship_pos[0])
                ys.append(ship_pos[1])
                file.write(f'{t / 3600:.2f} {modv:.2f}\n')

            modaccel = 6.67 * 10 ** -11 * m1 / ((ship_pos[0] - sun_pos[0]) ** 2 + (ship_pos[1] - sun_pos[1]) ** 2)
            length = ((sun_pos[0] - ship_pos[0]) ** 2 + (sun_pos[1] - ship_pos[1]) ** 2) ** 0.5
            accel = ((sun_pos[0] - ship_pos[0]) / length * modaccel, (sun_pos[1] - ship_pos[1]) / length * modaccel)
            phi = (accel[0] * v[0] + accel[1] * v[1]) / (
                    (accel[0] ** 2 + accel[1] ** 2) ** 0.5 * (v[0] ** 2 + v[1] ** 2) ** 0.5)
            modv = (v[0] ** 2 + v[1] ** 2) ** 0.5 + modaccel * phi * dt
            length = ((v[0] + accel[0] * dt) ** 2 + (v[1] + accel[1] * dt) ** 2) ** 0.5
            v = ((v[0] + accel[0] * dt), (v[1] + accel[1] * dt))
            ship_pos = (ship_pos[0] + v[0] * dt, ship_pos[1] + v[1] * dt)

    ax2.plot(xs, ys, label='my')
    plt.show()


def eve():
    # начальные параметры
    m1 = 1.2244 * 10 ** 23
    m2 = 21700
    ship_pos = (8.51 * 10 ** 7 * math.cos(math.pi / 54.8), 8.51 * 10 ** 7 * math.sin(math.pi / 54.8))
    modforce = 240 * 10 ** 3
    mass_decr = 15.8
    v = (-845.2, 0)
    phi = math.pi / 2

    # параметр дифферинцирования
    dt = 1

    fig3, ax3 = plt.subplots()

    xs = []
    ys = []

    # for p in count(0, 0.005):
    #     if p > 2 * math.pi:
    #         break
    #
    #     xs.append(7 * 10 ** 5 * math.cos(p))
    #     ys.append(7 * 10 ** 5 * math.sin(p))
    #
    # ax3.plot(xs, ys, label='ellipse')

    xs = []
    ys = []

    with open("data/eve_mod.txt", 'w', encoding="UTF-8") as file:
        for t in count(0, dt):
            if t < 2:
                modforce = 0
                mass_decr = 0
            elif t > 90000 or length - 7 * 10 ** 5 < 0:
                break
            elif length - 7 * 10 ** 5 < 5000:
                phi = teta - math.atan2(-v[1], -v[0])
                modforce = (10 ** -5 + 450 * (1 - ((length - 7 * 10 ** 5) / 90000) ** 0.5) ** 4) * (
                        v[0] ** 2 + v[1] ** 2) / 2 * 3.75 * 0.05
            elif length - 7 * 10 ** 5 < 90000:
                m2 = 700
                phi = teta - math.atan2(-v[1], -v[0])
                modforce = (10 ** -5 + 450 * (1 - ((length - 7 * 10 ** 5) / 90000) ** 0.5) ** 4) * (
                            v[0] ** 2 + v[1] ** 2) / 2 * 1.75 * 0.02
            elif 90000 > t > 85025:
                modforce = 0
                mass_decr = 0
            elif 85000 < t < 85025:
                modforce = 240 * 10 ** 3
                mass_decr = 15.8
            elif (v[0] ** 2 + v[1] ** 2) ** 0.5 < 2880:
                modforce = 0
                mass_decr = 0
            elif length - 7 * 10 ** 5 < 320000:
                modforce = 240 * 10 ** 3
                mass_decr = 15.8

            if 83500 < t < 90000:
                xs.append(t)
                ys.append((v[0] ** 2 + v[1] ** 2) ** 0.5)

                if t % 0.5 < dt:
                    file.write(f"{t - 83500:.2f} {(v[0] ** 2 + v[1] ** 2) ** 0.5:.2f}\n")

            modmg = 6.67 * (10 ** -11) * m1 * m2 / (ship_pos[0] ** 2 + ship_pos[1] ** 2)
            length = (ship_pos[0] ** 2 + ship_pos[1] ** 2) ** 0.5
            mg = (-ship_pos[0] / length * modmg, -ship_pos[1] / length * modmg)
            try:
                teta = math.atan2(-mg[1], -mg[0])
            except ZeroDivisionError:
                teta = math.pi / 2

            force = (modforce * math.cos(teta - phi), modforce * math.sin(teta - phi))

            accel = ((mg[0] + force[0]) / m2, (mg[1] + force[1]) / m2)
            v = (v[0] + accel[0] * dt, v[1] + accel[1] * dt)

            ship_pos = (ship_pos[0] + v[0] * dt, ship_pos[1] + v[1] * dt)

            m2 = m2 - mass_decr * dt

    ax3.plot(xs, ys)
    plt.show()


def main():
    # launch()
    # trans()
    # eve()


if __name__ == "__main__":
    main()
