a = input("please enter the yy-mm-dd:")
b = (31,28,31,30,31,30,31,31,30,31,30,31)

c = int(a[5])*10 + int(a[6])
d = int(a[-2])*10 + int(a[-1])
f = int(a[0])*1000 + int(a[1])*100 +int(a[2])*10 + int(a[3])

i = 0
e = 0
for i in range(c-1):
    e = e + b[i]

if((f%4 == 0) or(f%400 == 0)and (f%100 != 0)):
    e = e+d+1
else:
    e = e+d

print(e)


