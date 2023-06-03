#This program should not be included in the challenge this is just to help you set up the challenge
#It flags the flag input then does a ROT-13 encoding then base64 encoding to it.

# To make hidden files or directories all you have to do is put '.' in front of the name
#Example: 'mkdir .hidden_folder' or 'touch .hidden_file'

import base64

def rot13(text):
    result = ''
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            rotated = (ord(char) - ascii_offset + 13) % 26 + ascii_offset
            result += chr(rotated)
        else:
            result += char
    return result

text = "flag{ROT_13_4nd_b4s3_64}" #The flag
text = rot13(text) #ROT-13 the text
text = base64.b64encode(text.encode("utf-8")).decode('utf-8') #Base64 encode the text.

#Output flag (needs to be decoded as challenge)
print(text)
