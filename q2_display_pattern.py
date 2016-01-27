def display_pattern(n):
    for i in range(1, n+1):
        for j in range(n, i, -1):
            d = j // 10
            print(end = (d + 2) * " ")
        for k in range(i, 0, -1):
            print(k, end = " ")
        print("")


n = int(input("Enter a positive integer: "))
display_pattern(n)
