a = input("please enter the profit of the company:")
a = int(a)

if(type(a) == int):
	if(a <= 10):
	  s = a*0.1
	elif((a>10)and(a<=20)):
	  s = (a-10)*0.075 + 1
	elif((a>20)and(a<=40)):
	  s = (a-20)*0.05 + 1.75
	elif((a>40)and(a<=60)):
	  s = (a-40)*0.03 + 2.75
	elif((a>60)and(a<=100)):
	  s = (a-60)*0.015 + 3.35
	elif(a>100):
	  s = (a-100)*0.001+3.95
else:
  a = input("please enter a number again:")
