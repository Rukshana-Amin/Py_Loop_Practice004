if __name__=="__main__":

    num=int(input("Enter the number: "))

    i=0
    m=0

    for i in range(1,10+1,1):
        m=num*i

        print(num,"*",i,"=",m)
