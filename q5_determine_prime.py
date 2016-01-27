def is_prime(n):
    if n ==2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
                break
        if i == n - 1:
            return True

n = 2
for j in range(100):
    for k in range(10):
        while is_prime(n) == False:
            n = n + 1
        print("{0:<6d}".format(n),end = "")
        n = n + 1
    print("")


        
