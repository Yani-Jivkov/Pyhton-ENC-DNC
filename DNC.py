def DNC_logic(): # Main DNC logic
    crypt_word = input('Enter the crypted word => ')
    new_word = []

    # For loop
    for x in range(len(crypt_word)):
        char = crypt_word[x]
        char = ord(char) + (x + 1)
        new_word.append(chr(char))

    # Print
    print(''.join(new_word))

# Calling thu function
DNC_logic()
