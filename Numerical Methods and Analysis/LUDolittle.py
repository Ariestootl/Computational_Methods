import numpy as np
from scipy.linalg import lu

#Creating a Functio  for back substition
def backsub(U,z):
  N = U.shape
  x = np.zeros(N[0]); z = np.zeros(N[0]); v = np.zeros(N[0])
  y = np.zeros(N[0])
  for k in range(N[0] - 1, -1, -1):
    if U[k, k] == 0:
      break
      v[k] = z[k] / U[k, k]
      for c in range(k - 1, -1, -1):
        z[c] = z[c] - v[k] * U[c, k]
      y[k] = v[k]
      return y

#Creating a function for forward Substitution
def forsub(L,b):
  N = L.shape
  x = np.zeros(N[0]); z = np.zeros(N[0]); v = np.zeros(N[0])

  for j in range(N[0]):
    if L[j, j] == 0:
        break
    x[j] = b[j] / L[j, j]
    for i in range(j + 1, N[0]):
        b[i] = b[i] - L[i, j] * x[j]
    z[j] = x[j]
    return z

#Create a code for LU Factorization (Doolittle Algorithm)

#Initialization
A = np.array([[6, -2, -4, 4],[3, -3, -6, 1],[-12, 8, 21, -8], [-6, 0, -10, 7]]); b = np.array([2,-4,8,-43])
m, n = A.shape
N = A.shape
U = np.zeros(A.shape); L = np.zeros(A.shape)

#Doolittle Algorithm for LU Factorisation
for i in range(m):
    L[i,i] = 1

for i in range(len(A)):
    for j in range(i,len(A)):
        U[i,j] = A[i,j] - np.dot(L[i,0:i],U[0:i,j])
    for k in range(i+1, len(A)):
        L[k,i] = (A[k,i] - np.dot(L[k,0:i],U[0:i,i]))/U[i,i]


#Initialization for Forward and Backward Substitution
x = np.zeros(N[0]); z = np.zeros(N[0]); v = np.zeros(N[0])

# Forward Substitution
for j in range(N[0]):
    if L[j, j] == 0:
        break
    x[j] = b[j] / L[j, j]
    for i in range(j + 1, N[0]):
        b[i] = b[i] - L[i, j] * x[j]
    z[j] = x[j]



# Backward Substitution
y = np.zeros(N[0])

for k in range(N[0] - 1, -1, -1):
    if U[k, k] == 0:
        break
    v[k] = z[k] / U[k, k]
    for c in range(k - 1, -1, -1):
        z[c] = z[c] - v[k] * U[c, k]
    y[k] = v[k]


print("The solution vector x: ")
print(y)