import numpy as np

#writing the array /multidimentioanal array
arr =np.array([[1,3,4],[2,4,5]])

"""
basic numpy array operations
summation
addition/subtraction
multiplication and division
exponentiation
modulus operation
size
type
datatype of elements
shape
ndim 
item size in bytes
data type object
dtype()
reshape(new_shape

"""
#1. Size of the array
print("the array is of size: ",arr.size)

#2. Determining the type of variable arr is!
print("\nvariable arr is of type ",type(arr))

#3. Datatype of each element inside an array
print("\nDatatype of every element ",arr.dtype)

#4. Shape of the array as in gives the number or rows and columns it has
print("\nthe shape of this array :",arr.shape)


#5.Number of dimensions (rank) of a given array
print("\nthe rank of this array:",arr.ndim)

#6. Item size in Bytes
print("\nthe item size in byte for all",arr.nbytes)