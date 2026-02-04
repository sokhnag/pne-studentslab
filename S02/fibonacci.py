a = 0
b = 1
i = 2
lst = [a , b]
while i in range(11):
    new = a + b
    lst.append(new)
    a = b
    b = new
    i += 1
print(lst)