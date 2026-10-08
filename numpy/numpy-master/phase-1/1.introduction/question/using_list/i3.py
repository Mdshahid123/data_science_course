# creating a list with 1 crore element 

import time

list=[ i for i in range(1,100000000)]  #list comprehention



# print("before:",list)

# let's multiply each element with 2
start=time.time()
for i in range(0,4):
  list[i]=list[i]*2

end=time.time()
# print("after multiplication:",list)
print(f"time taken:{end-start:.6f}")


