n, m = map(int,input().split())
for i in range(1,m,2):
    if(i<n):
        print("-"*(int((m-(i*3))/2)),end='')
        print(".|."*(int(i)),end='')
        print("-"*(int((m-(i*3))/2))) 
print("-"*(int((m-7)/2)),end='')
print("WELCOME",end='')
print("-"*(int((m-7)/2)))
for i in reversed(range(1,m,2)):
    if(i<n):
        print("-"*(int((m-(i*3))/2)),end='')
        print(".|."*(int(i)),end='')
        print("-"*(int((m-(i*3))/2)))