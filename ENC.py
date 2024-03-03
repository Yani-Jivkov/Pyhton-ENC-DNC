def ENC_logic(): # Main ENC logic
    crypt_word = input('Enter the word => ')
    new_word = []
    # For loop
    for x in range(len(crypt_word)):
        char = crypt_word[x]
        char = ord(char) - (x + 1)

        new_word.append(chr(char))


    # Print
    print(f'Here is the crypted word =>', ''.join(new_word))

# Asking for the word to encrypt
ENC_logic()
