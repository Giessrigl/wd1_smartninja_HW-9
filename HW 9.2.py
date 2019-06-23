number = int(input("Enter a number between 1 and 50: "))

for x in range(1, 51):

    if (x != number) and (x % 3) == 0 and (x % 5) == 0:
        print("fizzbuzz")

    elif (x != number) and (x % 3) == 0:
        print("fizz")

    elif (x != number) and (x % 5) == 0:
        print("buzz")

    elif (x != number):
        print(x)

    else:
        break

if number % 3 == 0 and number % 5 == 0:
    print("fizzbuzz")

elif number % 3 == 0:
    print("fizz")

elif number % 5 == 0:
    print("buzz")

else:
    print(number)