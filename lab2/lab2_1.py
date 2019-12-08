# Dmitriy Uvin
import math
x = float(input('Enter x ( for angle it\'s will be in radians ): '))
y = float(input('Enter y: '))

deg = 2*x
sin = math.sin(deg)
ln = math.log(2*y + x)
f = sin/ln
print("F = {:.3f}".format(f))


