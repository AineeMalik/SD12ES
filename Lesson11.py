import math
Xa = float(input("Enter X coordinate for first point: "))
Ya = float(input("Enter Y coordinate for first point: "))
Xb = float(input("Enter X coordinate for Second point: "))
Yb = float(input("Enter X coordinate for Second point: "))

Distance = math.sqrt(((Xa-Xb)*(Xa-Xb))+((Ya-Yb)**2))

print(Distance)