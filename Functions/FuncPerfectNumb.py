def perfectnumb():
    list = []
    number = int(input("Please enter a number:"))
    sum = 0

    for i in range(1,number-1):
        if number % i == 0:
            list.append(i)
            sum += i

    if number == sum:
        print("This is a perfect number!")
    else:
        print("This is not a perfect number!")
        
perfectnumb()
 