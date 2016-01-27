def verify_input():
    if m > 0 and m == int(m) and n > 0 and n == int(n):
        return True
    else:
        return False

def gcd(m,n):
    if m >= n:
        while n != 0:
            d = m % n
            m = n
            n = d
        print(m)
    elif m < n:
        while n != 0:
            d = m % n
            m = n
            n = d
        print(m)

m = int(input("Enter a positive integer: "))
n = int(input("Enter another positive integer: "))

if verify_input():
    gcd(m,n)
else:
    print("Invalid input!")
