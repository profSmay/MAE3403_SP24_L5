# region imports
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
# endregion

# region functions
def ode_system(X, t,m,c,k,fmag):
    # define any numerical parameters (constants)
    # these params were stored in a list, and must be passed in the correct order!

    #define the forcing function equation
    f = fmag*np.sin(2*t)
    
    x = X[0]
    xdot=X[1]  # copy from the state array to nicer names
    
    #write the non-trivial equation
    xddot = (1/m) * (f-c*xdot-k*x)
       
    return [xdot,xddot]

def main():
    t = np.linspace(0, 10, 200)    #time goes from 0 to 10 seconds
    ic = [0,0]  # initial conditions

    #define the model parameters
    m = 1  # the mass
    c = 4  # damping (shock absorber)
    k = 16  # the spring
    fmag = 5  # the magnitude of the forcing function

    x1 = odeint(ode_system, ic, t, args=(m, c, k, fmag))

    c = 8
    x2 = odeint(ode_system, ic, t, args=(m, c, k, fmag))

    c = 32
    x3 = odeint(ode_system, ic, t, args=(m, c, k, fmag))

    plt.plot(t, x1[:,0],  label = 'c=4')
    plt.plot(t, x2[:,0],  label = 'c=8')
    plt.plot(t, x3[:,0],  label = 'c=32')
    plt.legend(loc = 'lower right')
    plt.xlabel('Time, s')
    plt.ylabel('Position')
    plt.title('Spring-Mass-Damper Dynamics - Forced Response')
    plt.show()
# endregion

# region function calls
if __name__ == "__main__":
    main()
# endregion