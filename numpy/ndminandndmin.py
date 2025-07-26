import numpy as np

#ndim
arr = np.array(3)
arr1 = np.array([1,2,3,4])
arr2 = np.array([[1,2,33,4] , [2,3,3,4]])
arr3 = np.array([[ [[1,2,34] , [2,3,454]]]])
print("the dimension is : " , arr.ndim)
print("the dimension is : " , arr1.ndim)
print("the dimension is : " , arr2.ndim)
print("the dimension is : " , arr3.ndim)

#ndmin
arr = np.array(3 , ndmin=5)
print(arr)
print("the dimension is  [modified size]: " , arr.ndim)

