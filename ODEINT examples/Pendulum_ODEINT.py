# region imports
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
# end region

# region functions
def ode_system(X, t, gc, L ):

    theta=X[0]; thetadot=X[1]  # copy from the state array to nicer names
    
    #write the non-trivial equation
    thetaddot= -gc/L * np.sin(theta)
       
    return [thetadot,thetaddot]

def main():
    t = np.linspace(0, 10, 200)    #time goes from 0 to 10 seconds
    ic=[1,0]

    #define the model parameters
    L = 2  # the mass
    gc = 9.81
    x = odeint(ode_system, ic, t,args=(gc,L))

    plt.plot(t, x[:,0], 'b-', label = 'Angular Position')
    plt.plot(t, x[:,1], 'r-', label = 'Angular Velocity')
    plt.legend(loc = 'lower right')
    plt.xlabel('Time, s')
    plt.ylabel('Angular Position and Velocity')
    plt.title('Simple Pendulum')
    plt.show()
# endregion

# region function calls
if __name__ == "__main__":
    main()
# endregion