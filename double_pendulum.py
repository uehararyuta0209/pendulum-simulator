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
        delta = theta1 - theta2
        mu = 2  # m1 = m2 = 1

        dtheta1_dt = omega1
        dtheta2_dt = omega2

        den = mu - np.cos(delta)**2

        domega1_dt = (
            g*(np.sin(theta2)*np.cos(delta) - mu*np.sin(theta1))
            - (l2*omega2**2 + l1*omega1**2*np.cos(delta))*np.sin(delta)
        ) / (l1 * den)

        domega2_dt = (
            g*mu*(np.sin(theta1)*np.cos(delta) - np.sin(theta2))
            + (mu*l1*omega1**2 + l2*omega2**2*np.cos(delta))*np.sin(delta)
        ) / (l2 * den)

        return [dtheta1_dt, domega1_dt, dtheta2_dt, domega2_dt]

    initial_state = [theta1, omega1, theta2, omega2]
    t_span = (0, duration)
    t_eval = np.linspace(0, duration, 1000)
    sol = solve_ivp(equations, t_span, initial_state, t_eval=t_eval)

    # 角度を -π ～ π に正規化
    theta1_out = np.arctan2(np.sin(sol.y[0]), np.cos(sol.y[0]))
    theta2_out = np.arctan2(np.sin(sol.y[2]), np.cos(sol.y[2]))

    return sol.t, theta1_out, theta2_out