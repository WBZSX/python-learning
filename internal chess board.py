a = ([],[],[],[],[],[],[],[])
for i in range(1,9):
	for j in range(1,9):
	  if((i+j)%2 == 0):
	    a[i-1].append('*')
	  else:
	    a[i-1].append('.')
	    
	print(a[i-1])


