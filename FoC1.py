#!/usr/bin/env python3

import math


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
    rsa(p,q)     


def rsa(p, q):
    n = p * q               # Calculate N
    phy = (p-1) * (q-1)     # Calculate phy(N)
    e = 0
    while ( e >= 0  &  e < phy ):
        if math.gcd(e,phy) == 1:
            pubk = e,n
            print("Public Key is : ",pubk)
            break
        else:
            e = e + 1 
    d = 0
    while ( d >= 0  &  d < phy ):
        if (d * e % phy) == 1:
            privk = d,n
            print("Private Key is : ",privk)
            break
        else:
            d = d + 1



prime_nos()