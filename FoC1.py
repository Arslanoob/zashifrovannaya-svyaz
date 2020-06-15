def prime_nos():
    sum = 0
    value = input ("Enter name\n")
    for x in value :
        sum = sum + ord(x)
    prime = sum
    i = 0
    while i<2:
        prime = prime + 1
        for n in range (2,prime):
            if (prime % n) == 0 :
                break
        else :
            i = i+1
            if i == 1 :
                p = prime
            elif i == 2 :
                q = prime
    return p,q     


def rsa(p, q):
    n = p * q
    phy = (p-1) * (q-1)
    i = 0
    while i != phy:
        




rsa(p,q)
print(func1())