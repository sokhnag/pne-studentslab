#a

def is_even(n):
    n = int(n)
    return n % 2 == 0

print(is_even(input("Enter a number: ")))

#b

def classify_triangle(a, b, c):
    if a == b == c:
        print("Equilateral")
    elif a == b or a == c:
        print("isosceles")
    else:
        print("scalene")

print(classify_triangle(5, 5, 5) , classify_triangle(3, 3, 4) , classify_triangle(3, 4, 5))