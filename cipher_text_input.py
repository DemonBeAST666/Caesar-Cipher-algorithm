def caesar_cipher(text, shift, decrypt=False):
    result=""

    if decrypt:
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_base=ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else: 
            result += char
    return result

#user input

message = input("Enter your message: ")
shift = int(input("Enter the shift: "))

#Encrypt the message
encrypted_message =caesar_cipher(message,shift)
print("Encrypted message: ",encrypted_message)

# Decrypted message
decrypted_message = caesar_cipher(encrypted_message, shift, decrypt=True)
print("Decrypted message: ",decrypted_message)
