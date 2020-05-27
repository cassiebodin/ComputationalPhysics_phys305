def gauss():
    import numpy as np

    A = np.array([[-3,2,-6],[5,7,-5],[1,4,-2]], dtype='float')
    b = np.array([6,6,8])

   
    Ab = np.hstack([A, b.reshape(-1, 1)])

    n = len(b)

    for i in range(n):
        a = Ab[i]

        for j in range(i + 1, n):
            b = Ab[j]
            m = a[i] / b[i]
            Ab[j] = a - m * b

    for i in range(n - 1, -1, -1):
        Ab[i] = Ab[i] / Ab[i, i]
        a = Ab[i]

        for j in range(i - 1, -1, -1):
            b = Ab[j]
            m = a[i] / b[i]
            Ab[j] = a - m * b

    x = Ab[:, 3]
    print (x)
gauss()
