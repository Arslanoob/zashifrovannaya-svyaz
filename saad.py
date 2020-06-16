#!/usr/bin/env python3
import socket as sk
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
    rsa(p, q)     


def rsa(p, q):
    n = p * q               # Calculate N
    phy = (p-1) * (q-1)     # Calculate phy(N)
    e = 2
    while ( e >= 0  &  e < phy ):
        if math.gcd(e,phy) == 1:
            pubk = e,n
            break
        else:
            e = e + 1 
    d = 2
    while ( d >= 0  &  d < phy ) :
        if (d * e % phy) == 1 & (d != e):
            privk = d,n
            x_s = d 
            send(3**d%17)
            x_s = d 
            return x_s
            break 
        else:
            d = d + 1

def dh(x_s,pub_A,a,g):
    k = (pub_A**x_s)%g
    return k


def send(cipher):
    final = bytes(cipher)
    s.sendall(final)
    print(' data sent')


def receive():
    data = s.recv(1024)
    print("\nMessage from A : " + data.decode('utf-8'))

def receive_key():
    data = s.recv(1024)
    pub_A = int(data.decode('utf-8'))  
    print("\nMessage from A : " + data.decode('utf-8'))
    dh(x_s,pub_A,3,17)

    


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1337  # The port used by the server
with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    prime_nos()
    receive_key()
    print(k)

