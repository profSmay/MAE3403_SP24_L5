# region imports
import numpy as np
from scipy import linalg
# endregion

# region functions
def main():
    """
    This tests the eigenvalue problem for a square matrix
    :return:
    """
    A=np.array([[5,3],[3,5]])
    ev = linalg.eig(A)
    print("Eigen Vector 1 = {}, $\lambda$ = {}".format(ev[0][0],ev[1][0]))
    aa=np.matmul(A,ev[1][0])
    AA=np.matmul(A,ev[1][1])

    bb=np.multiply(ev[0][0], ev[1][0])
    BB=np.multiply(ev[0][1], ev[1][1])

    //working an example from MAE3013
    A=np.array([[-1,1,0],[1,-2,1],[0,1,-1]])
    ev=linalg.eig(A)
    vec1=np.round(ev[1][:,0],2)
    vec1/=np.max(vec1)
    vec2=np.round( ev[1][:,1],2)
    vec2/=np.max(vec2)
    vec3=np.round( ev[1][:,2],2)
    vec3/=np.max(vec3)
    print("")
    print("Eigen Vector 1 = {}, $\lambda$ = {:.3f}".format(vec1,ev[0][0]))
    print("Eigen Vector 2 = {}, $\lambda$ = {:.3f}".format(vec2,ev[0][1]))
    print("Eigen Vector 3 = {}, $\lambda$ = {:.3f}".format(vec3,ev[0][2]))

    aa=np.matmul(A,ev[1][0])
    AA=np.matmul(A,ev[1][1])

    bb=np.multiply(ev[0][0], ev[1][0])
    BB=np.multiply(ev[0][1], ev[1][1])
    pass
# endregion

# region funciton calls
if __name__=="__main__":
    main()
# endregion