dict={'amazon':5,'adidas':10,'puma':14,'hero':20,}
max=max(dict.values())
m2=0
for v in dict.values():
	if v<max and v>m2:
	    m2=v
print('2nd max value is : ')
print(m2)
