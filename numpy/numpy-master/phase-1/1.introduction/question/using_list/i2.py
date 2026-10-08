# creating a list with 1 crore element 

import time

list=[]

for i in range(1,5):
  list.append(i)
print("before:",list)

# let's multiply each element with 2
start=time.time()
for i in range(0,4):
  list[i]=list[i]*2

end=time.time()
print("time taken:",end-start)
print("after multiplication:",list)



