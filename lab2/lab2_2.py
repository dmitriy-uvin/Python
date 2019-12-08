import math
m1 = float(input('Enter weight for the first planet (in tonnes): '))
m2 = float(input('Enter weight for the second planet (in tonnes): '))
m3 = float(input('Enter weight for the third planet (in tonnes): '))


d1 = float(input('Enter diameter for the first planet (in kilometers): '))
d2 = float(input('Enter diameter for the second planet (in kilometers): '))
d3 = float(input('Enter diameter for the third planet (in kilometers): '))

r1 = d1/2
r2 = d2/2
r3 = d3/2
print("First planet radius {:.7}".format(r1))
print("Second planet radius {:.7}".format(r2))
print("Third planet radius {:.7}\n".format(r3))

v1 = (4/3)*math.pi*r1*r1*r1
v2 = (4/3)*math.pi*r2*r2*r2
v3 = (4/3)*math.pi*r3*r3*r3

print("First planet volume {:.7} km^3".format(v1))      # volume = объем
print("Second planet volume {:.7} km^3".format(v2))
print("Third planet volume {:.7} km^3\n".format(v3))

p1 = m1/v1
p2 = m2/v2
p3 = m3/v3

print("First planet density {:.7} t/km^3".format(p1))    #density = плотность
print("Second planet density {:.7} t/km^3".format(p2))
print("Third planet density {:.7} t/km^3\n".format(p3))

m = max(p1, p2, p3)

if m == p3:
    print("The biggest density has planet number 3. \nHer density = {:.7} t/km^3".format(p3))
elif m == p1:
    print("The biggest density has planet number 1. \nHer density = {:.7} t/km^3".format(p1))
elif m == p2:
    print("The biggest density has planet number 1. \nHer density = {:.7} t/km^3".format(p2))

