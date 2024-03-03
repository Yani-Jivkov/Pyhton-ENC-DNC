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

# Help
print('Hello!')
print('This console program encrypts and decrypts words up to ten characters.')
print('If you want to encrypt type ENC, but if you want to decrypt type DNC.')
print('When you are done just type Exit!')

# While loop
while True:
    # Asking for the function
    function = input('Enter the function or type Exit => ')

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
