# region imports
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy
# endregion

# region functions
def twoQuadratics(vals): #vals is a list of 2 numbers  ???
    """
    Two quadratic equations are defined in this function
    One is the equation of a circle centered at 0,0:  x^2 + y^2 = r^2
    The other is the equation of a parabola through 0,1:  y=0.5*x^2+1
    Presumably, there are points where these equations intersect (i.e., roots of the set of equations).
    Step 1:  put each equation in the form where f(x)=0, where x is a vector.
    Step 2:  given an input vector (vals in this case), plug in values to get and output vector of the f(x) for each equation.
    :param vals: a tuple containing x and y
    :return:  a tuple of the solution to each equation
    """
    x, y = vals
    #  x^2  + y^2 = r^2  a circle of radius=4
    f1val = x**2+y**2-16  #  f1(x,y)=x^2  + y^2 - r^2  = 0 when correct x and y
    # y = 0.5*x^2 + 1
    f2val = 0.5*x**2 + 1 - y  # f2(x,y)=0.5*x^2 + 1 - y = 0 when correct x and y
    return (f1val, f2val)

def AnothertwoQuadratics(vals, radius=2, width=0.5, offset=1):
    """
    1st eqn:  This is for a circle centered at zero, but now radius is set from outside
    2nd eqn:  This is for a parabola with a y offset and width given in args
    :param vals: (x,y) as tuple
    :param args: list [radius, width, offset]
    :return: tuple with (f1val, f2val)
    """
    x, y = vals
    f1val = x**2+y**2-radius**2
    f2val = width*x**2 + offset - y
    return (f1val, f2val)

def fromNotes(vals):
    x,y=vals
    f1val=np.sin(x)-3*y
    f2val=np.exp(y)+np.cos(x)
    return (f1val,f2val)

def main():
    """
    This module demonstrates the use of FSOLVE for two equations.  Previously, we used FSOLVE to find the root
    of a single (perhaps complicated) equation/function.  Now, we have a pair of equations and we want to find the
    point(s) of intersection between these two equations.
    :return: nothing
    """

    # https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.optimize.fsolve.html
    (x,y)=fsolve(twoQuadratics,(1.2,0.4))
    print("\n\nFirst function, No args possible: ",x,y)
    f1val=x**2+y**2-16
    f2val=0.5*x**2 + 1 - y
    #let's plot it
    xvals=np.linspace(0,5,100)  # create the x values for the plot
    y_fn1=np.array([np.sqrt(-x**2+16) for x in xvals])  # calculate y values for plot of fn1
    y_fn2=np.array([0.5*x**2+1 for x in xvals])  # calculate y values for plot of fn2
    plt.plot(xvals,y_fn1)  # plot fn1
    plt.plot(xvals,y_fn2)  # plot fn2
    # plot a circle where the fn1 & fn2 intersect (x,y)
    plt.plot(x,y,marker='o', markerfacecolor='none', markeredgecolor='red', markersize=14)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(0,4)
    plt.xlim(0,4)
    ax=plt.gca()
    ax.tick_params(axis='both', direction="in")
    plt.grid()
    plt.show()

    Rgs=(4,0.2,1)
    radius, width, offset = Rgs
    (x,y)=fsolve(AnothertwoQuadratics,(1,1),Rgs)
    print("Second function, no Args sent: ",x,y)
    # let's plot it
    f1val=x**2+y**2-radius**2
    f2val=width*x**2 + offset - y
    xvals = np.linspace(0, 5, 100)
    y_fn1 = np.array([np.sqrt(-x ** 2 + radius**2) for x in xvals])
    y_fn2 = np.array([width * x ** 2 + offset for x in xvals])
    plt.plot(xvals, y_fn1)
    plt.plot(xvals, y_fn2)
    plt.plot(x, y, marker='o', markerfacecolor='none', markeredgecolor='red', markersize=14)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(0, 4)
    plt.xlim(0, 4)
    plt.show()

    (x, y) = fsolve(fromNotes, (-3, 0))
    print("fromNotes: ", x, y)
    #let's plot it
    xvals=np.linspace(-3.5,-2,100)
    y_fn1=np.array([1/3*np.sin(x) for x in xvals])
    y_fn2=np.array([np.log(-np.cos(x)) for x in xvals])
    plt.plot(xvals,y_fn1)
    plt.plot(xvals,y_fn2)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x,y,marker='o', markerfacecolor='none', markeredgecolor='red', markersize=14)
    plt.show()

    #find the other root
    (x, y) = fsolve(fromNotes, (-2, 0))
    print("fromNotes: ", x, y)
    #let's plot it
    xvals=np.linspace(-3.5,-2,100)
    y_fn1=np.array([1/3*np.sin(x) for x in xvals])
    y_fn2=np.array([np.log(-np.cos(x)) for x in xvals])
    plt.plot(xvals,y_fn1)
    plt.plot(xvals,y_fn2)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x,y,marker='o', markerfacecolor='none', markeredgecolor='blue', markersize=14)
    plt.show()
# endregion

# region function calls
if __name__ == "__main__":
    main()
# endregion