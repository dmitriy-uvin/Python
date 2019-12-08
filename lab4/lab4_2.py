import random as r
import numpy
rows = int(input("Enter the number of rows for matrix: "))   # rows
cols = int(input("Enter the number of cols for matrix: "))   # cols
ran_to = int(input("Enter the end of random range (Will be generated FROM 10 TO YOUR NUMBER): "))
matrix = [[r.randint(10, ran_to) for i in range(cols)] for j in range(rows)]
matrix = numpy.reshape(matrix, (rows, cols))
print("Matrix BEFORE: \n", matrix)
res = 0
results = []
for row in matrix:
    for item in row:
        f = item // 10
        s = item % 10
        summa = f + s
        res = item % summa
        results.append(res)
results = numpy.reshape(results, (rows, cols))
print("Matrix AFTER: \n", results)