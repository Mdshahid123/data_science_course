# 2-D ARRAY

# A NumPy array that contains one-D  elements 
# syntax: np.array([ele1,ele2,ele3...) where ele1,ele2,ele3 should be one dimention list
# shape means number of elements  along each dimension.
# size means sum of all primitive elements


import numpy as np

arr1 = np.array([
    []
    
])


print(f"arr1:{arr1},size:{arr1.size},shape:{arr1.shape}")

arr2 = np.array([
    [10,20,30,40],
    [20,30,40,50],
    
])

print(f"arr2:{arr2},size:{arr2.size},shape:{arr2.shape}")

arr3 = np.array([
    [10,20,30,40],
    [20,30,40,50],
    [40,50,40,50],
    
])

print(f"arr3:{arr3},size:{arr3.size},shape:{arr3.shape}")
