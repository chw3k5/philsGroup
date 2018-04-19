import numpy as np

print("Starting script")

# This is comment


g_m_per_s2 = 9.807
def calc_torque(mass, lever_len, angle=90.0):
    torque = g_m_per_s2 * float(mass) * float(lever_len) * np.sin(float(angle))
    return torque

def calc_inertia(mass, rad, rot_axis, a=(1/4), b=(1/3)):
    inertia = (a * float(mass) * float(rad) ** 2) + (b * float(mass) * float(rot_axis) ** 2)
    return inertia


for theta in range(0, 90):
    def calc_ang_accel(rad):
        ang_accel = float(g_m_per_s2) / (float(rad) * np.sin(float(theta)))
        print(theta)
        return ang_accel


if __name__ == "__main__":
    print("max torque: ")
    print(calc_torque(1.6, 2))
    print("inertia: ")
    print(calc_inertia(1.6, 3, 5))
    print(calc_ang_accel(1.5))
    print("This is the end of the script, good job.")

