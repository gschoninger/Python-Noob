import math

a = 0.2 #int(input())
b = 2
c = 1

if a!= 0:
	x1 = (-b +math.sqrt(b**2 -4*a*c))/(2*a)
	x2 = (-b -math.sqrt(b**2 -4*a*c))/(2*a)
	print("x1 : ", x1)
	print("x2 : ", x2)
else: 
	print("a must be different than zero!")

