def numb():
    numbers = []
    for i in range(10):
        number=int(input("Please enter a number:"))
        numbers.append(number)
    print(numbers)

    maxnumber=max(numbers)
    print("Max number is:",maxnumber)

    upperlimit=int(input("Please enter a upper limit:"))
    print("Upper limit is",upperlimit)

    for i in range(0,upperlimit+1,2):
        print(i)

    lowerlimit = int(input("Please enter a lower limit:"))


    for i in range(lowerlimit, upperlimit+1):
        if i % 2 == 0:
           print("Even numbers:",i)

numb()