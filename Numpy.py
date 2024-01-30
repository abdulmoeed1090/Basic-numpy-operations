import numpy as np

# dimensions of arrays will be same as number of brackets
a = np.array([1, 2, 3])
# printing the array
print('a',a)
# printing the dimensions of array
print('dimensions of a :',a.ndim)
b = np.array([[2.3, 4.5, 2.1], [2.3, 43.3, 90.0]])
c = np.array([[1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7, 8]])
# printing the array
print('b',b)
print ('c',c)
# printing the dimensions of array
print('dimensions of b :',b.ndim)
# printing the data type
print('datatype of b :',b.dtype)
# printing the order of array
print('order of b :',b.shape)
# accesing the elements
print(b[0, 2])
# acessing the row
print(b[0, :])
# acessing the column
print(b[:, 2])
# getting a little more fancy[start:end:step-size
print(c[1, 0:6:1])
# changing one element
a[1]=90
print(a)
# changing a column
c[:,2]=0
print(c)
# changing a row
c[1,:]=0
print(c)
