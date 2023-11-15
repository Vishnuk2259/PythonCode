import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

#ENCRYPT

plain_text = input("Enter the string you want to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]
    
print(f"Orginal text  : {plain_text}")
print(f"Encypted text : {cipher_text}")

#DECRYPT

cipher_text = input("Enter the string you want to decrypt: ")
plain_text = ""

for letter  in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]
    
print(f"Encypted text  : {cipher_text}")
print(f"Decrypted text : {plain_text}")