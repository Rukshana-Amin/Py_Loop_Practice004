if __name__=="__main__":
    
    n = int(input("Input Upper Limit: "))

    sum = 0
    i=0
    while i<=n:
        if i%2!= 0:
            sum += i
        i += 1
    print("sum =", sum)
