def jollyJumper(lis):
    length = len(lis)
    lis1 = set(range(1,length))
    for i in range(length-1):
        b = abs(lis[i+1]-lis[i])
        if  (0<b<=(length-1)) and b in lis1:
            lis1.remove(b)
    print lis1
    if len(lis1)==0:
        return "list is a jolly jumper"
    else:
        return "not a jolly jumper"




lis = [11, 7, 4, 2, 1, 6]
print jollyJumper(lis)

