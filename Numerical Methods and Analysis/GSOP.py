import numpy as np
from scipy.linalg import lu
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
def gram_schmidt(vector_list):
    """"
    Gram-Schmidt Orthonormalization Process
    """
    orthovs = []
    for i in range(len(vector_list)):
        vector = vector_list[i]
        for j in range(i):
            vector -= np.dot(vector, orthovs[j])*orthovs[j]
        norm = np.linalg.norm(vector)
        if norm == 0:
            raise ValueError("The given vectors are linearly dependent.")
        orthov = vector / norm
        orthovs.append(orthov)
    return orthovs

#Testing the Algorithm
vector_list = [[1,1,1,1],[0,1,1,1],[0,0,1,1]]
A = np.array(vector_list).T

#QR Decomposition
gs = gram_schmidt(vector_list)
Q = np.array(gs).T
R = np.dot(Q.T,A)
print("QR Decomposition of the Matrix A: ",A)
print("The Matrix Q: ", Q)
print("The Matrix R: ", R)
