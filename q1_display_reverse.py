def reverse_int(n):
    if n == 0:
        print(0)
    else:
        k = 0
        digit = [0 for i in range(100)]
        while n != 0:
            digit[k] = n % 10
            n //= 10
            k = k + 1
        for i in range(k):
            print(digit[i], end="")

n = int(input("Enter a non-negative integer: "))
reverse_int(n)
