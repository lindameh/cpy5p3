def convert_ms(n):
    n = n / 1000
    hour = int(n // 3600)
    n = n % 3600
    minute = int(n // 60)
    n = n % 60
    second = int(n)
    print("{0}:{1}:{2}".format(hour,minute,second))

n = float(input("Enter milliseconds: "))
convert_ms(n)
