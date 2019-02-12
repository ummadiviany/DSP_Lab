import matplotlib.pyplot as plt
import numpy as np
n=input('Enter n Value:')
result=[]
for i in range(n):
	result.append(1)
a1=plt.subplot(2,1,1)
plt.title("Accumulator")
plt.xlabel('time')
plt.ylabel('....u[n]......')
plt.stem(result)
out=[]
out.append(1)
for x in range(n):
	if(x>0):
		out[x]=result[x]+out[x-1]
		print('I am executed')
	out.append(out[x])
out.remove(out[-1])
plt.subplot(2,1,2)
plt.xlabel('time')
plt.ylabel('Accumulator')
plt.stem(out,shareax=a1)
plt.show()