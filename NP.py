import numpy as np
a=np.array([(1,2,3),(4,5,6)])
print(a.ndim)
print(a.itemsize)
print(a.dtype)
print(a.size)
print(a.shape)
#reshape n slicing:
a=np.array([(1,2,3,4,5),(3,6,7,8,9)])
print(a[0,2])
print(a[1:, 3])

a=np.linspace(1,3,5)
print(a)
print(a[0: 2])

import numpy as np
a=np.array([(1,2,3),(4,5,6)])
print(a.sum(axis=0))
print(np.sqrt(a))
print(np.std(a))
