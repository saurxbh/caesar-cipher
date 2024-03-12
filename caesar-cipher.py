'''
The caesar cipher is a shift cipher that uses addition and subtraction to encrypt and decrypt letters.
'''

try:
    import pyperclip # pyperclip copies the text to clipboard
except ImportError:
    pass # If pyperclip is not installed, do nothing, it's no biggie.

# Every possible symbol that can be encrypted or decrypted. Here, we are using only letters.
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print('Caesar cipher')
print('''
The caesar cipher encrypts letters by shifting them over by a
key number. For example, a key of 2 means the letter A is
encrypted into C, B into D, and so on.''')
print()

# Let the user enter whether they are encrypting or decrypting
while True: # Keep asking until user enters e or d
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

# Let the user enter the key to use
while True: # Keep asking until the user enters a valid key
    maxKey = len(SYMBOLS) - 1
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# Let the user enter the message to encrypt/decrypt
print('Enter the message to {}'.format(mode))
message = input('> ').upper()




