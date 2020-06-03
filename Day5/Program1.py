def replace_no(num):
	return int(str(num).replace('0','5'))
	
num=int(input('enter the no. : '))
print('after replacing the no. is : ', replace_no(num))
