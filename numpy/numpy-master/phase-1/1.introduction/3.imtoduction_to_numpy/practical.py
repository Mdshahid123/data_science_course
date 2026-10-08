
import numpy as np
import time

# Create a NumPy array of numbers from 1 to 1000

arr = np.arange(1, 1001)

# Measure execution time
start = time.time()
print("Start:", start)

total = np.sum(arr)

end = time.time()
print("End:", end)

print("Sum:", total)
print("Time taken:", end - start, "seconds")



# so Instead of storing  in a Python list, we use a NumPy array because it is:

# Faster
# Uses less memory
# Supports mathematical operations directly

