def fibosum(n):
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
    return sum(lst)

print("Sum of the first 5 terms:", fibosum(5))
print("Sum of the first 10 terms:", fibosum(10))