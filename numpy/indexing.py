import numpy as ar
arr = ar.array([1,2,3,34,5])

#indexing the values of the one dimensional array
print(arr[0]) #1

arr2 = ar.array([[1,2,3,4] , [1,2,3,3]])
print(arr2[0,-1]) #4

#slicing
print(arr2[1, 0:2])
print(arr2[0:2 , 0:3])

arr3 = ar.array([[[1,2,3,4],[1,2,3,3]] , [[1,2,2,3] ,[22,3,4,5]]])
print(arr3)
print(arr3[1,1,-1])

#slicing
print(arr3[0:2 , 0:1 , 0:2])

