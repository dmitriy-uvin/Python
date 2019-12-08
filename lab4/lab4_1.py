import random as r
e1 = int(input("Enter number of elements for the first list: "))
e2 = int(input("Enter number of elements for the second list: "))
d1 = int(input("Number FROM: "))
d2 = int(input("Number TO: "))
first = [r.randint(d1, d2) for i in range(e1)]
second = [r.randint(d1, d2) for j in range(e2)]
print("LIST BEFORE: {0}".format(first))
third = []
for i in range(len(first)):
    third.append((first[i], second[i]))
for i in first:
    for j in second:
        if i == j:
            print("Element - {0}, index(first) - {1}, index(second) - {2}".format(i, first.index(i), second.index(j)))
            ind = first.index(i)
            first[ind] = 0
            break
third = list(zip(first, second))
print("LIST AFTER: {0}\nLIST with TUPLES: {1}".format(first, third))

