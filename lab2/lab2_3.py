N = int(input("Enter the number bigger than 100: "))
if N > 100:
    array = list(range(10, N+1))
    for i in array:
        n_l = int(len(str(i)))
        if n_l % 2 == 0:
            half = int(n_l/2)
            left_part = str(i)[:half]
            right_part = str(i)[::-1]
            right_part = right_part[:half]
        else:
            half = int((n_l-1) / 2)
            left_part = str(i)[:half]
            right_part = str(i)[::-1]
            right_part = right_part[:half]

        if left_part == right_part:
            print("Number {0} is symmetrical.".format(i))
else:
    print("ERROR! Number less than 100!")
