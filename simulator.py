import numpy as np
from scipy.integrate import solve_ivp# Convert angle from degrees to radians
def simulator(length, angle_deg, duration):
    angle_rad = np.radians(angle_deg)
    
    # Initial conditions
    d = duration
    g = 9.81
    l = length
    theta = angle_rad
    omega = 0.0

    # Time span for the simulation
    t_span = (0, d)
    
    # Define the equations of motion
    def equations(t, state):
        theta, omega = state
        dtheta_dt = omega
        domega_dt = -(g/l) * np.sin(theta)
        return [dtheta_dt, domega_dt]

    # Initial state vector
    initial_state = [theta,omega]
    
    # Solve the equations of motion
    solution = solve_ivp(equations, t_span, initial_state, t_eval=np.linspace(0, duration, num=100))
    
    return solution.t, solution.y[0], solution.y[1]
    
if __name__ == "__main__":
    t, theta, omega = simulator(length=1.0, angle_deg=30.0, duration=10.0)
    print(f"計算した時刻の数: {len(t)}")
    print(f"最初の角度: {theta[0]:.4f} rad")
    print(f"最大角度:   {max(theta):.4f} rad")
    print(f"最小角度:   {min(theta):.4f} rad")