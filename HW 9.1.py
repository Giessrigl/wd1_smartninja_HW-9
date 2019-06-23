user_name = input("What´s your name? ")
print("Hello " + user_name + ", i will convert kilometers into miles for you!")

while True:
    km = int(input("Enter amount of kilometers: "))
    miles = km /1.609
    print(str(km) + " kilometers are " + str(miles) + " miles!")

    ask = input("Do you want to do another conversion? (y/n): ")

    if ask == "n":
        print("Goodbye " + user_name)
        break