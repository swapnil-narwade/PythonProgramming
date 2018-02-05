import sys
import os
encrypttext = open("cypher.txt", 'r')
line = encrypttext.read()
list2 = list('abcdefghijklmnopqrstuvwxyz')
list1 = list('dxjkrcvstzwbphqgiumeaylnof')
decipher = []


def append(x):
    decipher.append(x)
    return decipher


def main():
    for i in line:
        for j in list1:
            if i.lower() == j:
                k = list1.index(i)
                append(list2[k])
    decrypt_file = ''.join(decipher)
    output = open("decipher.txt", 'w')
    output.write(decrypt_file)

main()

