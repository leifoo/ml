import numpy as np

# scalar (0D tensor)
x = np.array(12)
print('x = ', x)
print('# of dimensions=', x.ndim)

# vector (1D tensor)
y = np.array([12, 3, 6, 14])
print('y = ', y)
print('y.ndim = ', y.ndim)

# matrices (2D tensor)
z = np.array([[5, 78, 2, 34, 0],
              [6, 79, 3, 35, 1],
              [7, 80, 4, 36, 2]])
print('z = \n', z)
print('z.ndim = ', z.ndim)

# 3D tensors and higher-dimensional tensors
a = np.array([[[5, 78, 2, 34, 0],
               [6, 79, 3, 35, 1],
               [7, 80, 4, 36, 2]],
              [[5, 78, 2, 34, 0],
               [6, 79, 3, 35, 1],
               [7, 80, 4, 36, 2]],
              [[5, 78, 2, 34, 0],
               [6, 79, 3, 35, 1],
               [7, 80, 4, 36, 2]]])
print('a.ndim  = ', a.ndim)
print('a.shape = ', a.shape)
print('a.dtype = ', a.dtype)

# Element-wise operations
print('y+1 = ', y + 1)
print('np.maximum(z, 1.) = \n', np.maximum(z, 1.))

# Tensor dot (tensor product)
print('np.dot(y, y) = ', np.dot(y, y))
print('np.dot(z[:, :-1], y) = ', np.dot(z[:, :-1], y))

# Tensor reshaping
print('z.reshape(5, 3) = \n', z.reshape(5, 3))
print('np.transpose(z) = \n', np.transpose(z))
