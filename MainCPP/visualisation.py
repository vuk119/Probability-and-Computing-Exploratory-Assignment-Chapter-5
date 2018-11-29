import matplotlib.pyplot as plt
import numpy as np
import os

input = np.loadtxt("./Main/data2.txt", dtype='d', delimiter=' ')

n=input[:,0]
N=1<<(n.astype(int))
N=N-1
print(N)
means=input[:,1]
stds=input[:,2]

print(input)


limit=15

plt.scatter(N[0:limit],means[0:limit], label="data points")
plt.errorbar(N[0:limit],means[0:limit],yerr=stds[0:limit],linestyle='none')

#plt.plot(N[0:limit],0.5*N[0:limit]*np.log(N[0:limit]), label="$\\frac{1}{2} \\cdot N \\cdot log(N)$", zorder=-1)
plt.plot(N[0:limit],N, label="$ N $", zorder=-1)


plt.title("$Average \\ number \\ of \\ steps \\ versus \\ size \\ of \\ the \\ tree$")

plt.xlabel("$N \\ where \\ size \\  is \\ 2^N-1 $")
plt.yticks([(means[0:limit])[0],(means[0:limit])[-3],(means[0:limit])[-2],(means[0:limit])[-1]],
 np.round([0,means[0:limit][-3]/10**3,means[0:limit][-2]/10**3,means[0:limit][-1]/10**3],3))

plt.ylabel("$Average \\ number \\ of \\ steps \\ [10^3]$")

plt.legend()

plt.show()
