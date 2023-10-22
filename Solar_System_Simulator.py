import matplotlib.pyplot as plt
import math

au = 149.6e9 # Astronomical Unit 
G = 6.6743e-11 # Gravitational constant in metre cubed divided by kilogram second square
timestep = 86400.0 # Approximately one revolution on earth

mass = [1.989e30, 0.33e24, 4.869e24, 5.974e24, 0.647e24] # Mass of the Sun, Mercury, Venus, Earth and Mars in kilograms, respectively
x = [0, 0.387*au, 0.723*au, 1*au, 1.524*au] # Position  of the Sun, Mercury, Venus, Earth and Mars in metres alone the x-axis, respectively
y = [0, 0, 0, 0, 0] # Position  of the Sun, Mercury, Venus, Earth and Mars in metres alone the y-axis, respectively
vx = [0, 0, 0, 0, 0] # Velocity of the Sun, Mercury, Venus, Earth and Mars in metres per second alone the x-axis, respectively
vy = [0, 47.36e3, 35.02e3, 29.78e3, 24.07e3] # Velocity of the Sun, Mercury, Venus, Earth and Mars in metres per second alone the y-axis, respectively
a_x = [0, 0, 0, 0, 0]# Acceleration of the Sun, Mercury, Venus, Earth and Mars in metres per second squared alone the x-axis, respectively
a_y = [0, 0, 0, 0, 0]# Acceleration of the Sun, Mercury, Venus, Earth and Mars in metres per second squared alone the y-axis, respectively

def pyth(i, j):
   return math.sqrt((x[j]-x[i])**2 + (y[j]-y[i])**2)

plt.ion()  # Turning on interactive mode
fig, ax = plt.subplots()  # Creating a figure and axis

while True:
    for i in range(5):
        a_x[i] = 0
        a_y[i] = 0
        for j in range(5):
            if i == j:
                continue
            a_x[i] += G * ((mass[j])/(pyth(i, j)**3)) * (x[j] - x[i])
            a_y[i] += G * ((mass[j])/(pyth(i, j)**3)) * (y[j] - y[i])

    for i in range(5):
        vx[i] += a_x[i] * timestep
        vy[i] += a_y[i] * timestep

        x[i] += vx[i] * timestep
        y[i] += vy[i] * timestep

    ax.clear()  # Clear the current plot
    ax.scatter(x, y, color='blue', marker='.')
    ax.set_ylim(-2.5e11, 2.5e11)
    ax.set_xlim(-2.5e11, 2.5e11)
    plt.pause(0.001)

    # Kill switch: break the loop if the plot window is closed
    if not plt.fignum_exists(fig.number):
        break

plt.ioff()  # Turn off interactive mode

    