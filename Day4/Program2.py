
from operator import itemgetter
item=[('a','b','c'),('f','a','b'),('g','h','a'),('b','b','c')]
N=1
print('before sorting list is: ',item)
item.sort(key=itemgetter(N))
print('After sorting list is : ',item)
