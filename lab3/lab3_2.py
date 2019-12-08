mn = 1
while True:
    numbers = input("Enter 11 numbers with a space: ").strip()
    try:
        numbers = list(map(int, numbers.split(" ")))
    except:
        print("You entered the letter or double number!")
    else:
        if len(numbers) == 11:
            for k in numbers:
                mn *= k
            print(abs(mn))
            break
        else:
            print("You entered incorrect quantity of numbers! Try again!")
