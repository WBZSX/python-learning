a = (1,2,3,4)
b = []
for x in a:
    for y in a:
	    if(x == y):
		    continue
	    else:
		    for z in a:
			    if(z == x):
				    continue
			    elif(z == y):
				    continue
			    else:
				    d = x*100 + y*10 + z
				    b.append(d)
print(b)
