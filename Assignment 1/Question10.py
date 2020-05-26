def geometric(a,b):
    i=0
    while i<10:
        print(a)
        a = a*b
        i+=1
geometric(int(input("Enter first term of the series ")),int(input("Enter Common Ratio ")))