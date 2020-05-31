#armstrong no. 
n=int(input('enter the no. :'))
a=n
r=0
while(n>0):
	k = n% 10
	r=r+ k*k*k
	n=n//10
if(r==a):
	print('no. is armstrong')
else:
	print('no. is not armstrong')
