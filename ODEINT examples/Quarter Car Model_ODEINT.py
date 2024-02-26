# region imports
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
# endregion
def ode_system(X, t, carparams, roadparams):
    #define any numerical parameters (constants)
    # these params were stored in two lists, and must be passed in the correct order!
    #carparams, roadparams = args
    m1=carparams[0]; m2=carparams[1]; c1=carparams[2]; k1=carparams[3]; k2=carparams[4]
    
    ymag=roadparams[0]
    
    #define the forcing function equation
    if t < np.pi/2:
        y=ymag*np.sin(2*t)
    else:
        y=0
    
    x1=X[0]; x1dot=X[1]; x2=X[2]; x2dot=X[3] # copy from the state array to nicer names
    
    #write the non-trivial equations
    x1ddot= (1/m1) * (c1*(x2dot-x1dot)+k1*(x2-x1))
    x2ddot= (1/m2) * (-c1*(x2dot-x1dot)-k1*(x2-x1)+k2*(y-x2))
    
    #return the derivitaves of the input state vector
    return [x1dot,x1ddot,x2dot,x2ddot]

def main():
    t = np.linspace(0, 20, 200)    #time goes from 0 to 10 seconds
    ic=[0,0,0,0]

    #define the model parameters
    m1=1  # the mass
    m2=1
    c1=6  # damping (shock absorber)
    k1=1 # the spring
    k2=4
    ymag = 1 # the magnitude of the forcing function
    carparams=[m1,m2,c1,k1,k2]  #put the car parameters into a list
    roadparams=[ymag] #put the road parameters into a list

    sln = odeint(ode_system, ic, t, args=(carparams,roadparams))

    plt.plot(t, sln[:,0], 'b-', label = 'Body Position')
    plt.plot(t, sln[:,1], 'r-', label = 'Body Velocity')
    plt.legend(loc = 'lower right')
    plt.xlabel('Time, s')
    plt.ylabel('Position and Velocity')
    plt.title('Car Body Dynamics')
    plt.show()

    plt.plot(t, sln[:,2], 'b-', label = 'Wheel Position')
    plt.plot(t, sln[:,3], 'r-', label = 'Wheel Velocity')
    plt.legend(loc = 'lower right')
    plt.xlabel('Time, s')
    plt.ylabel('Position and Velocity')
    plt.title('Car Tire Dynamics')
    plt.show()

main()