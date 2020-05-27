#Cassandra Bodin
#phys305
#Homework 8

#run using " python hmk8_bodin.py"

#Problem 1: use Gaussian elimination method to solve following matrix. Ax=b, where A = [[-3,2,-6],[5,7,-5],[1,4,-2]] b=[6,6,8]
#note used code from http://mlwiki.org in order to figure out a simple way to implement Gaussian Elimination

def Problem1():
    import numpy as np
    import math
    

    def Gauss():
        import numpy as np

        A = np.array([[-3,2,-6],[5,7,-5],[1,4,-2]], dtype='float')
        b = np.array([6,6,8])

   #makes an augmented 2x1 matrix of A and b
        Ab = np.hstack([A, b.reshape(-1, 1)])

        n = len(b)

#reduces to upper triangular matrix (0's below each pivot) also called echelon form
        for i in range(n):
            a = Ab[i]


            for j in range(i + 1, n):
                b = Ab[j] 
                m = a[i] / b[i] 
                Ab[j] = a - m * b

#reduces matrix further to row echelon form, also called normaliing the matrix
        for i in range(n - 1, -1, -1):
            Ab[i] = Ab[i] / Ab[i, i]
            a = Ab[i]


#cycles through each row and reduces it given information from the other rows
            for j in range(i - 1, -1, -1):
                b = Ab[j]
                m = a[i] / b[i]
                Ab[j] = a - m * b

#recombines each reduced row back into a matrix/vector
        x = Ab[:, 3]
        print ("Using Gaussian elimination x is:", x)
    Gauss()


#check using linalg
    A = np.array([[-3,2,-6],[5,7,-5],[1,4,-2]])
    b = np.array([6,6,8])
    x1=np.linalg.tensorsolve(A,b)
    print("Using linalg to check, x is:", x1)
Problem1()

print("____________________________________________________________________")

#Problem 2: Calculate Moment of inertia tensor for rectangle  m=1,a=1,b=2. sigma = m/A where A=a*b, sigma = 1/2. Find the eigenvalues and eigenvectors for the moment of inertia tensor using linalg.

def Problem2():
    import math
    import matplotlib.pyplot as plt
    import numpy as np


    I = np.array([ [4/3, -1/2, 0], [-1/2, 1/3, 0], [0, 0, 5/3] ])

    u,v=np.linalg.eig(I)
    print ("eigenvalues are: ",u)
    print ("eignevectors are: " ,v)
Problem2()

print("____________________________________________________________________")


#Problem 3: use the relaxation/Jacobi method to  model infinite plate capacitor in a box

def Problem3():
    import numpy as np 
    import matplotlib.pyplot as plt
    import matplotlib.colors as colors
    from mpl_toolkits import mplot3d

# Constants
    m = 10         # number of points
    Vtop = 0.0      # boundary conditions
    Vbot = 0.0
    Vleft = 0.0
    Vright = 0.0
    target = 1e-6   # Target accuracy

# Create arrays to hold potential values
    phi = np.zeros([m+1,m+1],float)
    phi[m,:] = Vtop 
    phi[0,:] = Vbot 
    phi[:,m] = Vright
    phi[:,0] = Vleft  
    phiprime = np.zeros([m+1,m+1],float)
    zdata = np.zeros([m+1,m+1],float)

# Main loop
    deltaV = 1.0
    while deltaV>target:
        deltaV = 0.
    # Calculate new values phiprime of the potential
    # in terms of the old values phi

        for i in range(m+1):
            for j in range(m+1):
#set conditions for edge of box
                if (i==m or i==0 or j==m or j==0):
                    phiprime[i,j]=phi[i,j]
#set the conditions for capacitor inside box
                elif (i==m-3 or i==3):
                    phiprime[m-3,:] =100
                    phiprime[3,:] = -100
                    phiprime[:,0] = Vleft
                    phiprime[:,m] = Vright
    # calculate new values phiprime of the potential in terms of the old values phi 
                else:
                    phiprime[i,j]= (1/4)*(phi[i+1,j]+phi[i-1,j]+phi[i,j+1]+phi[i,j-1])
    # calculate some difference to use for convergence
                deltaV += abs(phiprime[i,j]- phi[i,j])

    #print(deltaV)
                phi, phiprime = phiprime, phi

    zdata = phiprime

    np.set_printoptions(formatter={'float': '{: 0.2f}'.format})
    for i in range(m,-1,-1):
        print (zdata[i,:])

#plot data, kept both plots since it uses a different color plot method
    fig, ax = plt.subplots(1,2)
    pcm = ax[0].pcolormesh(zdata, cmap='jet')
    fig.colorbar(pcm, ax=ax[0])
    ax[0].set_title('pcolormesh')
    ax[0].set_xlabel('x axis')
    ax[0].set_ylabel('y axis')

    levels = 15
    cf = ax[1].contourf(zdata, levels=levels,cmap='jet') 
    fig.colorbar(pcm, ax=ax[1])
    ax[1].set_title('contourf with levels')
    ax[1].set_xlabel('x axis')
    ax[1].set_ylabel('y axis')

    fig.savefig('plate_capacitor.png')
    fig.tight_layout()
    plt.show()
Problem3()
