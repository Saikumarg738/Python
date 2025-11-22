import numpy as np
import sys


b=list(range(10000))

print(sys.getsizeof(b))

a=np.array(b)

#print(sys.getsizeof(a))
print(a.nbytes)