n = int(input("enter level of pyramid: "))

def pattern(x):
    if(x==1):
        print('*')
    else:
        i = 1
        for i in range(1,x + 1):
            print('*',end=" ")
        print(' ')
        pattern(x-1)
pattern(n)