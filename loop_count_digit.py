if __name__=="__main__":

    num=int(input ("Enter Digits= "))

    count=0

    if num < 0:
        num = -1*num

    if num == 0:

        count = 1
        
    while num!=0:
        
        num = num // 10
        count += 1
            
        print("Count of digits: ", count)
