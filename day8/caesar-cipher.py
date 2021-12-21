from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(text2, shift2, direction2):
    cipher_text = ""
    new_position = 0
    for letter in text2:
        if letter in alphabet:
            alphabet_position = alphabet.index(letter)
            if direction2 == "encode":
                new_position = alphabet_position + shift2
            elif direction2 == "decode":
                new_position = alphabet_position - shift2
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"The {direction2}d text is: {cipher_text}")




should_end = True

while should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text2=text, shift2=shift, direction2=direction)
    result = input(f"Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "yes":
        should_end = True
    else:
        should_end = False

