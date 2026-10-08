# 3-d array:
# A NumPy array that contains two-D  items 
# shape means number of items  along each dimension.
# size means sum of all primitive item

import numpy as np

arr1=np.array([
     [[1,234,80]],
  ])

print(f"arr1:{arr1},size:{arr1.size},shape:{arr1.shape}")

arr2=np.array([
     [[1,234,80]],
     [[1,234,80]],
  ])

print(f"arr1:{arr1},size:{arr1.size},shape:{arr1.shape}")



arr3=np.array([
     [[1,234,80]],
     [[1,234,80]],
     [[1,234,80]],
     [[1,234,80]],
  ])

print(f"arr1:{arr1},size:{arr1.size},shape:{arr1.shape}")



arr3=np.array([
     [[1,234,80],[10,20,40]],
     [[1,234,80],[50,60,5]],
     [[1,234,80],[1,3,2]],
     [[1,234,80],[2,5,7]],
  ])

print(f"arr1:{arr1},size:{arr1.size},shape:{arr1.shape}")
