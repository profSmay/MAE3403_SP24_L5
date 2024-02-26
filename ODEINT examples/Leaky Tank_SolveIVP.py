# region imports
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
# endregion

# region functions
def ode_system(t, x):
    #define any numerical parameters (constants)
    qvi=24  # input flow rate
    cdA2g=6 # cd * Area* sqrt(2g)
    A=1     # Tank cross-sectional area
    
    h=x[0]
    hdot=(1/A)*(qvi-cdA2g*np.sqrt(h))
    return [hdot]

def main():
    t = np.linspace(0, 10, 200)    #time goes from 0 to 10 seconds
    h0 = np.zeros(1)               # and array to hold the initial conditions
    h0[0]=0

    sln = solve_ivp(ode_system,[0,10], h0, t_eval=t)

    plt.plot(sln.t, sln.y[0], 'b-', label = 'Fluid Height')
    plt.legend(loc = 'lower right')
    plt.xlabel('Time, s')
    plt.ylabel('Fluid Height, m')
    plt.title('Filling a Leaky Tank')
    plt.show()
# endregion

# region funciton calls
if __name__ == "__main__":
    main()
# endregion