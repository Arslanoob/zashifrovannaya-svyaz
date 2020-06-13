def func1():
    sum = 0
    value = input ("Enter name\n")
    for x in value :
        sum = sum + ord(x)
    bum = sum
    i = 0
    while i<2:
        bum=bum+1
        for n in range (2,bum):
            if (bum % n) == 0 :
                break
        else :
            i = i+1
            if i == 1 :
                p=bum
            elif i == 2 :
                q = bum
    return p,q;


print(func1())