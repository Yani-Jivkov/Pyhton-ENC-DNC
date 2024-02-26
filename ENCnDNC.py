def ENC_logic(): # Main ENC logic
    crypt_word = input()
    new_word = []
    # For loop
    for i in range(len(crypt_word) + 1):
        if i == 1:
            char1 = ord(crypt_word[0])
            char1 -= 1
            char1 = chr(char1)
            new_word.append(char1)
        elif i == 2:
            char2 = ord(crypt_word[1])
            char2 -= 2
            char2 = chr(char2)
            new_word.append(char2)
        elif i == 3:
            char3 = ord(crypt_word[2])
            char3 -= 3
            char3 = chr(char3)
            new_word.append(char3)
        elif i == 4:
            char4 = ord(crypt_word[3])
            char4 -= 4
            char4 = chr(char4)
            new_word.append(char4)
        elif i == 5:
            char5 = ord(crypt_word[4])
            char5 -= 5
            char5 = chr(char5)
            new_word.append(char5)
        elif i == 6:
            char6 = ord(crypt_word[5])
            char6 -= 6
            char6 = chr(char6)
            new_word.append(char6)
        elif i == 7:
            char7 = ord(crypt_word[6])
            char7 -= 7
            char7 = chr(char7)
            new_word.append(char7)
        elif i == 8:
            char8 = ord(crypt_word[7])
            char8 -= 8
            char8 = chr(char8)
            new_word.append(char8)
        elif i == 9:
            char9 = ord(crypt_word[8])
            char9 -= 9
            char9 = chr(char9)
            new_word.append(char9)
        elif i == 10:
            char10 = ord(crypt_word[9])
            char10 -= 10
            char10 = chr(char10)
            new_word.append(char10)


    # Print
    print(''.join(new_word))

def DNC_logic(): # Main DNC logic
    crypt_word = input()
    new_word = []

    # For loop
    for i in range(len(crypt_word) + 1):
        if i == 1:
            char1 = ord(crypt_word[0])
            char1 += 1
            char1 = chr(char1)
            new_word.append(char1)
        elif i == 2:
            char2 = ord(crypt_word[1])
            char2 += 2
            char2 = chr(char2)
            new_word.append(char2)
        elif i == 3:
            char3 = ord(crypt_word[2])
            char3 += 3
            char3 = chr(char3)
            new_word.append(char3)
        elif i == 4:
            char4 = ord(crypt_word[3])
            char4 += 4
            char4 = chr(char4)
            new_word.append(char4)
        elif i == 5:
            char5 = ord(crypt_word[4])
            char5 += 5
            char5 = chr(char5)
            new_word.append(char5)
        elif i == 6:
            char6 = ord(crypt_word[5])
            char6 += 6
            char6 = chr(char6)
            new_word.append(char6)
        elif i == 7:
            char7 = ord(crypt_word[6])
            char7 += 7
            char7 = chr(char7)
            new_word.append(char7)
        elif i == 8:
            char8 = ord(crypt_word[7])
            char8 += 8
            char8 = chr(char8)
            new_word.append(char8)
        elif i == 9:
            char9 = ord(crypt_word[8])
            char9 += 9
            char9 = chr(char9)
            new_word.append(char9)
        elif i == 10:
            char10 = ord(crypt_word[9])
            char10 += 10
            char10 = chr(char10)
            new_word.append(char10)

    # Print
    print(''.join(new_word))

# Help
print('Hello!')
print('This console program encrypts and decrypts words up to ten characters.')
print('If you want to encrypt type ENC, but if you want to decrypt type DNC.')
print('When you are done just type Exit!')

# While loop
while True:
    # Asking for the function
    function = input()

    # Checking for end
    if function == 'Exit':
        break

    # Checking if the function if ENC (encrypting)
    if function == 'ENC':
        # Calling
        encrypted_word = ENC_logic()

    # Checking if the function if DNC (decrypting)
    elif function == 'DNC':
        decrypted_word = DNC_logic()

    # Checking if it's not ENC or DNC
    else:
        print('Error')

