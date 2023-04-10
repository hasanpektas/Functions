def fib():
    Fibonacci=[1,1]

    n=int(input("Please enter terms number of list:"))

    if n<20:
        print("This value is smalller than 20!")
    else:
        while len(Fibonacci) < n:  
             nextnumber = Fibonacci[-1] + Fibonacci[-2]  
             Fibonacci.append(nextnumber)  

    print(Fibonacci)  

fib()
