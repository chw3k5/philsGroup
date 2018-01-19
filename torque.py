import numpy as np

print("Starting script")

# This is comment


g_m_per_s2 = 9.807
def calc_toque(mass, lever_len, angle=90.0):
    torque = g_m_per_s2 * float(mass) * float(lever_len) * np.sin(float(angle))
    return torque


if __name__ == "__main__":
    print(calc_toque(1.6, 2))
    print("This is the end of the script, good job.")
