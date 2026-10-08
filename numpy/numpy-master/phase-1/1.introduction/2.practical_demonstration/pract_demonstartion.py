
# let's suppose we have a list of n natural number  and calcuate it's summ

#lets create a list of n natural number 
import time
list=[]
for i in range(1,1001):
    list.append(i)

#print(list)

# now lets  calculate a it's sum 
sum=0
start=time.time()

for i in range(0,1000):
    sum=sum+list[i]

end=time.time()
print(sum)
print(f"time taken:{end-start:.6f}")


#  conculustion
#  more the numerical data more will be calculation time 

# that means if we have large amount of numerical data in data analytica and data science and we need to perofrm a mathmetcial calculation on them then we  should not  use python data structure instead we use numpy array