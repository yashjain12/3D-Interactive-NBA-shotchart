import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
import matplotlib.animation as animation
def getParabola(x_init, y_init):
    theta_initial = np.pi/3
    x_i, y_i, z_i = x_init, y_init, 0
    if x_i == 0:
        x_i = 0.01
    if y_i == 0:
        y_i == 0.01
    x_range, y_range = np.linspace(x_i, 0, 30), np.linspace(y_i, 0, 30)
    t_range = -np.sqrt(np.square(x_range) + np.square(y_range))

    a_poly = (t_range[0] * np.tan(theta_initial) + 10)/(t_range[0]**2)
    b_poly = -np.tan(theta_initial) - 20/t_range[0]
    c_poly = 10
    z_range = a_poly * np.square(t_range) + b_poly * t_range + c_poly
    parabolic_coord = np.concatenate((x_range[None].T, y_range[None].T, z_range[None].T), axis = 1)
    return parabolic_coord
def update_lines(num, walks, lines, shotsPerRep, shotchartmakes):
    #frame 303 = int(303/50)
    #going through every 50 lines
    #repetitions = int(np.ln(len(walks))) + 1
#        num_steps = 50 * repetitions
    currRep = int(num/30)
    for line, walk, make in zip(lines[shotsPerRep * currRep: min(shotsPerRep * (currRep + 1) - 1, len(walks) - 1)], 
                            walks[shotsPerRep * currRep: min(shotsPerRep * (currRep + 1) - 1, len(walks) - 1)], 
                            shotchartmakes[shotsPerRep * currRep: min(shotsPerRep * (currRep + 1) - 1, len(walks) - 1)]):
        line.set_data_3d(walk[num%30 + 1: num%30+6, :].T)
        if make:
            line.set_color('green')
        else:
            line.set_color('red')
            line.set_alpha(0.8)
    return lines