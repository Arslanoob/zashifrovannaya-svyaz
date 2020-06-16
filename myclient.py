#!/usr/bin/env python3
import socket as sk
def key(message):
    k = 0
    for ch in message:
        k = k + ord(ch)
    k = round((k / len(message))) % 26
    print('Key is  : ', k)
    return k


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


def receive():
    data = s.recv(1024)
    print("\nMessage from A : " + data.decode('utf-8'))


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1337  # The port used by the server

with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    name = sk.gethostname()
    k = key(name)
    encrypt(name, k)
    while True :
        ff = input("message new : ")
        encrypt(ff,k)
