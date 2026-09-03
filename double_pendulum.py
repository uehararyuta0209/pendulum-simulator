import numpy as np
from scipy.integrate import solve_ivp

def double_pendulum(l1, l2, angle1_deg, angle2_deg, duration, b=0.5):
    g = 9.81
    theta1 = np.radians(angle1_deg)
    theta2 = np.radians(angle2_deg)
    omega1 = 0.0
    omega2 = 0.0

    def equations(t, state):
        theta1, omega1, theta2, omega2 = state
        delta = theta2 - theta1  # ✅ 修正

        dtheta1_dt = omega1
        dtheta2_dt = omega2

        den = 3 - np.cos(2 * delta)

        domega1_dt = (-3*g*np.sin(theta1)
                      - g*np.sin(theta1 - 2*theta2)
                      - 2*np.sin(delta)*(omega2**2*l2 + omega1**2*l1*np.cos(delta))
                      ) / (l1 * den)

        domega2_dt = (2*np.sin(delta)*(
                      omega1**2*l1*2        # ✅ 修正
                      + 2*g*np.cos(theta1)  # ✅ 修正
                      + omega2**2*l2*np.cos(delta))
                      ) / (l2 * den)

        return [dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt]

    initial_state = [theta1, omega1, theta2, omega2]
    t_span = (0, duration)
    t_eval = np.linspace(0, duration, 1000)
    sol = solve_ivp(equations, t_span, initial_state, t_eval=t_eval)

    return sol.t, sol.y[0], sol.y[2]