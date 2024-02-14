alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Creating a funtion to encrypt the message
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"The encoded text message is: {cipher_text}")


# Creating a function to decrypt the message
def decrypt(cipher_text, shift_amount):
    shift_amount *= -1
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"The decoded text message is: {plain_text}")


from art import logo
print(logo)

is_on = True
while is_on:
    direction = input("Type encode to 'encrypt' and decode to 'decrypt':\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encrypt":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decrypt":
        decrypt(cipher_text=text, shift_amount=shift)
    else:
        print("ERROR!!!...Wrong direction")
    
    choice = input("Do you want to use the program again ?: ").lower()
    if choice == "no":
        is_on = False
    else:
        is_on = True

