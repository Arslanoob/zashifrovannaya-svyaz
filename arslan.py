#!/usr/bin/env python3
# conn.sendall(data)

import socket
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
            x_a = d 
            send(3**d%17)
            x_a = d 
            return x_a
            break 
        else:
            d = d + 1


def send(cipher):
    final = bytes(cipher, 'utf-8')
    conn.sendall(final)
    print('Encrypted data sent')

def dh(x_a,pub_s,a,g):
    k = (pub_s**x_a)%g
    return k

def receive_key(x_a):
    data = conn.recv(64)
    pub_s = int(data.decode('utf-8'))  
    print("\nMessage from A : " + data.decode('utf-8'))
    dh(x_a,pub_s,3,17)



HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 1337  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print('Connected by', addr)
    pub_s = conn.recv(1024)
    print(pub_s.decode('utf-8'))
    print(receive_key(prime_nos))