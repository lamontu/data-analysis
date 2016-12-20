# -*- coding: utf-8 -*-

import numpy as np
from numpy.linalg import det, inv, qr

x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
c1 = np.ones(3)
print("x:")
print(x)
print("y:")
print(y)
print("c1")
print(c1)
print("""
## x.dot(y), 2 two-dimension array x, y, dim 1 of x == dim 0 of y,
    return the product of matrices""")
print(x.dot(y))
print("""
## np.dot(x, c1)), two-dimension array and one-dimension array,
    dim 1 of x == dim 0 of y,
    return the inner product of each row with c1""")
print(np.dot(x, c1))

print("""
## np.inner(x, c1),
    x.shape: (dim-0, dim-1, ..., dim-m)
    c1.shape: (dim-0, dim-1, ..., dim-n)
    dim-m == dim-n 
    return the inner product of x with y over the last dimension""")
print(np.inner(x, c1))
print("### np.inner(x, c1).shape == x.shape[:-1] + c1.shape[:-1]")
print(np.inner(x, c1).shape)
print("### x.shape[:-1]:")
print(x.shape[:-1])
print("### c1.shape[:-1]:")
print(c1.shape[:-1])

print("## np.inner(x, x):")
print(np.inner(x, x))
print()

print("Compute the determinant of an array:")
mat = x.T.dot(x)
print("mat:")
print(mat)
print("det(mat):")
print(det(mat))
print()

print("## Compute the inverse of a matrix:")
print("a:")
a = np.array([[1., 2.], [3., 4.]])
print(a)
print("inv(a):")
print(inv(a))
print("a.dot(inv(a)):")
print(a.dot(inv(a)))

print("## Compute the qr factorization of a matrix:")
A = np.random.randn(16).reshape(4, 4)
print("A:")
print(A)
print(det(A))
print("Q, R = qr(A) ...") 
Q, R = qr(A)
print("Q:")
print(Q)
print("R:")
print(R)
print(det(Q))
print("det(Q):")
print(det(Q))
print("Q[0,:].dot(Q[1,:]):")
print(Q[0, :].dot(Q[1, :]))
print("Q[:, 0].dot(Q[:, 1]):")
print(Q[:, 0].dot(Q[:, 1]))
