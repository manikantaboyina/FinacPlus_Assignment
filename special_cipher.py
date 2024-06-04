""" 
Problem 1:
Write a special cipher that is a combination of Caesar’s cipher followed by a simple
RLE. The function should receive a string and the rotation number as parameters.
Input: special Cipher(“AABCCC”, 3) Output: D21EF3 

"""


# Solution:

def caesar_cipher(text, shift):
    ciphered_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            elif char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            ciphered_text += chr(shifted)
        else:
            ciphered_text += char
    return ciphered_text

def run_length_encoding(text):
    encoded_text = ""
    count = 1
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            encoded_text += f"{text[i]}{count}"
            count = 1
    encoded_text += f"{text[-1]}{count}"

    return encoded_text

def special_cipher(text, rotation_number):
    caesar_text = caesar_cipher(text, rotation_number)
    encoded_text = run_length_encoding(caesar_text)
    return encoded_text

input_text = input("Enter the string: ")
rotation_number = int(input("Enter the rotation number: "))
output_text = special_cipher(input_text, rotation_number)

print(f"Input: special Cipher('{input_text}', {rotation_number})")
print(f"Output: {output_text}")


# OUTPUT: (for example)
"""
Enter the string: AABCCC
Enter the rotation number: 3
Input: special Cipher('AABCCC', 3)
Output: D2E1F3

"""