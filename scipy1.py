import numpy as np
from scipy import sparse

b1 = np.eye(4, dtype=int)

print("Numpy 배열: \n{}".format(b1))

sparse_matrix1 = sparse.csr_matrix(b1)
print("Scipy의 CSR 행렬1: \n{}".format(sparse_matrix1))

b2= np.eye(5,k=-1,dtype=int)
print(b2)

sparse_matrix2 = sparse.csr_matrix(b2)
print("Scipy의 CSR 행렬2: \n{}".format(sparse_matrix2))

b3 = np.arange(16).reshape(4,4)
print(b3)

x= np.diag(b3)
print(x)

y= np.diag(np.diag(b3))
print("--------\n{}".format(y))

sparse_matrix3 = sparse.csr_matrix(y)
print("Scipy의 CSR 행렬3: \n{}".format(sparse_matrix3))

data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)

eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("COO 표현 : \n{}".format(eye_coo))