
import numpy as np
import matplotlib.pyplot as plt

pos = np.array([0.0, 0.0])
vel = np.array([10.0, 20.0])
acc = np.array([0.0, -9.8])
dt = 0.1

x_val = []
y_val = []

for t in np.arange(0, 3, dt):
    vel += acc * dt
    pos += vel * dt
    x_val.append(pos[0])
    y_val.append(pos[1])

plt.plot(x_val, y_val)
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.title("Projectile Motion")
plt.grid()
plt.show()




