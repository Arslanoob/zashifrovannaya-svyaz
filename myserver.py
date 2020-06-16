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
            print("Public Key is : ",pubk)
            break
        else:
            e = e + 1 
    d = 2
    while ( d >= 0  &  d < phy ) :
        if (d * e % phy) == 1 & (d != e):
            privk = d,n
            print("Private Key is : ",privk)
            break
        else:
            d = d + 1

def encrypt(plaintext, n):
    key = 'abcdefghijklmnopqrstuvwxyz'
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    send(result.lower())



def send(cipher):
    final = bytes(cipher, 'utf-8')
    s.sendall(final)
    print('Encrypted data sent')

def keyfinder(cipher) -> int:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for key in range(len(letters)):
        text = ''
        for symbol in cipher:
            if symbol in letters:
                num = letters.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(letters)
                text = text + letters[num]
            else:
                text = text + symbol
        print("KEY #{} : {}".format(key, text))
    a = int(input("Enter Key to chat"))
    return a


def decrypt(ciphertext, n):
    key = 'abcdefghijklmnopqrstuvwxyz'
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 1337  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(1024)
    k = keyfinder(data.decode('utf-8'))
    print("[+] Key Determined for secure chat")
    while True:
        ndata = conn.recv(4048)
        ndata = ndata.decode('utf-8')
        print(decrypt(ndata, k))
