n = int(input("enter number of commands: ")) #take number of commands to operate on list
l = [] #create the list
for _ in range(n):
    s = input().split() #user inputs first command and its arguments in the format ---> insert 1 5
    cmd = s[0] #seperate out commanding key word
    args = s[1:] #seperate out arguments
    if cmd !="print":
        cmd += ("(") + (",".join(args)) + (")") # a = ","   a.join(args) will give 1,5 just it's done without declaring a
        eval("l."+cmd) #string concatination is done directly without assigning it to a variable
    else:
        print(l)