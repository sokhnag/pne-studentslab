def fibon(n):
    a = 0
    b = 1
    i = 2
    lst = [a, b]
    while i in range(n):
        new = a + b
        lst.append(new)
        a = b
        b = new
        i += 1
    return lst[-1]

print("The fifth term of the Fibonacci sequence is:  " , fibon(5))
print("The tenth term of the Fibonacci sequence is:  " , fibon(10))
print("The fifteenth term of the Fibonacci sequence is:  " , fibon(15))