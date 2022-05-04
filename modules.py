#h stock and v stack
import numpy as np
x=np.array([1,2,3])
y=np.array([6,7,8])
print(np.vstack((x,y)))
print(x.ravel())
#numpy functions
import numpy as np
import matplotlib_practice  as plt
x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show()