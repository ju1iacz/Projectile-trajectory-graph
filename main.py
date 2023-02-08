import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

def projectile(V_init, theta, S, m, H, drag=True):
    g = 9.81 #gravitational acceleration
    C = 0.47 #drag coefficient
    air = 1.2 #air density

    time = np.linspace(0, 100, 10000)
    tof = 0
    dt = time[1] - time[0]
    gravity = -g * m
    V_ix = V_init * np.cos(theta) #speed in the x axis
    V_iy = V_init * np.sin(theta) #speed in the y axis
    v_x = V_ix
    v_y = V_iy
    r_x = 0 #position in the x axis
    r_y = H #position in the y axis
    r_xs = list()
    r_ys = list()
    r_xs.append(r_x)
    r_ys.append(r_y)

    for t in time:
        F_x = 0.0
        F_y = 0.0
        if (drag == True):
            F_y = F_y - 0.5*C*S*air*pow(v_y, 2)
            F_x = F_x - 0.5*C*S*air*pow(v_x, 2) * np.sign(v_y)
        F_y = F_y + gravity

        r_x = r_x + v_x * dt + (F_x / (2 * m)) * dt**2
        r_y = r_y + v_y * dt + (F_y / (2 * m)) * dt**2
        v_x = v_x + (F_x / m) * dt
        v_y = v_y + (F_y / m) * dt

        if (r_y >= 0):
            r_xs.append(r_x)
            r_ys.append(r_y)
        else:
            tof = t
            r_xs.append(r_x)
            r_ys.append(r_y)
            break

    return r_xs, r_ys, tof

root = Tk()

###############
vlabel = Label(root, text = "Enter the initial speed [m/s]: ")
vlabel.grid(row = 0, column = 0)
v = StringVar()
v_t = Entry(root, width = 30, textvariable = v)
v_t.grid(row = 1, column = 0)

thetalabel = Label(root, text = "\nEnter the firing angle: ")
thetalabel.grid(row = 2, column = 0)
theta = StringVar()
theta_t = Entry(root, width = 30, textvariable = theta)
theta_t.grid(row = 3, column = 0)

hlabel = Label(root, text = "\nEnter the initial height [m]: ")
hlabel.grid(row = 4, column = 0)
h = StringVar()
h_t = Entry(root, width = 30, textvariable = h)
h_t.grid(row = 5, column = 0)

mlabel = Label(root, text = "\nEnter the mass of the projectile [kg]: ")
mlabel.grid(row = 6, column = 0)
m = StringVar()
m_t = Entry(root, width = 30, textvariable = m)
m_t.grid(row = 7, column = 0)

rlabel = Label(root, text = "\nEnter the projectile diameter [mm]: ")
rlabel.grid(row = 8, column = 0)
r = StringVar()
r_t = Entry(root, width = 30, textvariable = r)
r_t.grid(row = 9, column = 0)

def click():
    V = float(v.get())
    Theta = int(theta.get())
    Theta = np.radians(Theta)
    H = float(h.get())
    M = float(m.get())
    R = float(r.get())
    R = R / 2000
    S = np.pi * pow(R, 2)

    #trajectory graph
    fig = plt.figure(figsize=(10, 5))
    r_xs, r_ys, tof = projectile(V, Theta, S, M, H, True)
    plt.plot(r_xs, r_ys, 'b:', label="Gravity and air resistance")
    r_xs, r_ys, tof = projectile(V, Theta, S, M, H, False)
    plt.plot(r_xs, r_ys, 'k:', label="Gravity")
    plt.title("Trajectory", fontsize=14)
    plt.xlabel("Distance [m]")
    plt.ylabel("Height [m]")
    plt.ylim(bottom=0.0)
    plt.xlim(left=0.0)
    plt.legend()
    plt.show()

mylabel = Label(root, text = "       ").grid(row = 4, column = 1)
start = Button(root, text = "Generate trajectory", command = click)
start.grid(row = 4, column = 2)

root.mainloop()