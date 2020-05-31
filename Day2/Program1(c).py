#palindrome no.
n=int(input('enter the no. :'))
temp=n
rev=0
while(n>0):
	k=n%10
	rev=rev*10+k
	n=n//10
if(temp==rev):
	print('no. is palindrome')
else:
	print('no. isnt palindrome')
