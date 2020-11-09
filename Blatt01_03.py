print("Enter temperature in Fahrenheit : ")
F = input()
zustand = F
C = (5/9)*(int(F) - 32)
if C <= 0:
    zustand = "fest"
elif C > 0 and C < 100:
    zustand = "fluessig"
elif C > 100:
    zustand = "gasfoermig"
    
print("Temperature in Celsius: ",C)
print("State of matter: ", zustand)