#program for prime no.
n=int(input('enter the requd no. :'))
if n>1 :
	for i in range(2,n):
		if (n%i==0):
			print('no. is not prime')
			break
	else:
		     print('no. is prime')
else:
	print('no. is neither prime nor composite')
