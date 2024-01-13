# Asking for the word to encrypt
crypt_word = input()

# For loop
for i in range(len(crypt_word) + 1):
    if i == 1:
        char1 = ord(crypt_word[0])
        char1 -= 1
        char1 = chr(char1)
    elif i == 2:
        char2 = ord(crypt_word[1])
        char2 -= 2
        char2 = chr(char2)
    elif i == 3:
        char3 = ord(crypt_word[2])
        char3 -= 3
        char3 = chr(char3)
    elif i == 4:
        char4 = ord(crypt_word[3])
        char4 -= 4
        char4 = chr(char4)
    elif i == 5:
        char5 = ord(crypt_word[4])
        char5 -= 5
        char5 = chr(char5)
    elif i == 6:
        char6 = ord(crypt_word[5])
        char6 -= 6
        char6 = chr(char6)
    elif i == 7:
        char7 = ord(crypt_word[6])
        char7 -= 7
        char7 = chr(char7)
    elif i == 8:
        char8 = ord(crypt_word[7])
        char8 -= 8
        char8 = chr(char8)
    elif i == 9:
        char9 = ord(crypt_word[8])
        char9 -= 9
        char9 = chr(char9)
    elif i == 10:
        char10 = ord(crypt_word[9])
        char10 -= 10
        char10 = chr(char10)

    # Prints
    if len(crypt_word) == 1:
        print(f'{char1}')
    elif len(crypt_word) == 2:
        print(f'{char1}{char2}')
    elif len(crypt_word) == 3:
        print(f'{char1}{char2}{char3}')
    elif len(crypt_word) == 4:
        print(f'{char1}{char2}{char3}{char4}')
    elif len(crypt_word) == 5:
        print(f'{char1}{char2}{char3}{char4}{char5}')
    elif len(crypt_word) == 6:
        print(f'{char1}{char2}{char3}{char4}{char5}'
                f'{char6}')
    elif len(crypt_word) == 7:
        print(f'{char1}{char2}{char3}{char4}{char5}'
                f'{char6}{char7}')
    elif len(crypt_word) == 8:
        print(f'{char1}{char2}{char3}{char4}{char5}'
                f'{char6}{char7}{char8}')
    elif len(crypt_word) == 9:
        print(f'{char1}{char2}{char3}{char4}{char5}'
                f'{char6}{char7}{char8}{char9}')
    elif len(crypt_word) == 10:
        print(f'{char1}{char2}{char3}{char4}{char5} '
                f'{char6}{char7}{char8}{char9}{char10}')
