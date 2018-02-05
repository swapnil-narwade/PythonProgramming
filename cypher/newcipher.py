#import sys
#import os
#filename = input("enter the filename you want to save")
#plaintext_file = open(filename, 'a')
#content = input("enter the content you want to add in your file")
#plaintext_file.write(content)
#plaintext_file.close()
#read_file = open(filename, 'r')
#line = read_file.read()
list1 = list('abcdefghijklmnopqrstuvwxyz')
list2 = list('dxjkrcvstzwbphqgiumeaylnof')
cipher = []
def append_cipher(x):
    cipher.append(x)
    return cipher


def main():
    for i in line:
        for j in list1:
            if i.lower() == j:
                k = list1.index(j)
                append_cipher(list2[k])
    ciphertext = ''.join(cipher)
    print("Plaintext =", line)
    print("cipher text is =", ciphertext)

#file = open("cypher.txt", "w")
#file.write(cyphertext)
#file.close()
#read_file.close()