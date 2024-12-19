import numpy as np
def mnk(x,y):
    x = np.array(x)
    y = np.array(y)
    a = ((x*y).mean() - x.mean()*y.mean())/((x*x).mean() - x.mean()**2)
    b = y.mean() - a*x.mean()
print(mnk([1,2,3,4,5],[1,2,3,4,5]))
