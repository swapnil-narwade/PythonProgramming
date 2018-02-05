#name : swapnil narwade
#uta_id :1001396025
#Assignment 1
plaintext = "security is often important"
list1 = list('abcdefghijklmnopqrstuvwxyz')
list2 = list('dxjkrcvstzwbphqgiumeaylnof')
cipher = []
decrypt = []


def append_cipher(x):
    cipher.append(x)
    return cipher


def append_decrypt(x):
    decrypt.append(x)
    return decrypt


def main():
    for i in plaintext:
        for j in list1:
            if i.lower() == j:
                k = list1.index(j)
                append_cipher(list2[k])
    ciphertext = ''.join(cipher)
    print("Plaintext =", plaintext)
    print("cipher text is =", ciphertext)
    for i in cipher:
        for j in list2:
            if i.lower() == j:
                k = list2.index(j)
                append_decrypt(list1[k])
    decrypttext = ''.join(decrypt)
    print("\n\ncipher text is =", ciphertext)
    print("Plaintext =", decrypttext)


main()
