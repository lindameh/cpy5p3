def verify_input():
    if n == int(n) and n > 0:
        return True
    else:
        return False

def print_matrix(n):
    import random
    for i in range(n):
        for j in range(n):
            print(random.randint(0,1), end = " ")
        print("")

n = int(input("Enter a positive integer:"))
if verify_input():
    print_matrix(n)
else:
    print("Invalid input!")
