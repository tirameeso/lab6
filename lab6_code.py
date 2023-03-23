# Angely Gomez, 3/22/23
def password_encoder(password):
    encoded_pass = ""
    for number in password:
        encoded_pass += password_encoder_dict(number)
    return encoded_pass


def password_encoder_dict(password):
    encoded = {'0':'3', '1':'4', '2':'5', '3':'6', '4':'7', '5':'8', '6':'9', '7':'0', '8':'1', '9':'2'}
    return encoded[password]


def decoder(password):
    new_string_decoded = ''
    for digit in password:
        if int(digit) > 3:
            new_number = int(digit) - 3
            new_string_decoded += str(new_number)
        elif digit == '0':
            digit = '7'
            new_string_decoded += digit
        elif digit == '1':
            digit = '8'
            new_string_decoded += digit
        elif digit == '2':
            digit = '9'
            new_string_decoded += digit
    return new_string_decoded


if __name__ == "__main__":
    encoded_user_pass = ''
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        option = int(input('Please enter an option: '))

        if option == 1:
            user_pass = input('Please enter your password to encode: ')
            encoded_user_pass = password_encoder(user_pass)
            print('Your password has been encoded and stored!\n')

        elif option == 2:
            decoded_password = decoder(encoded_user_pass)
            print(f"The encoded password is {encoded_user_pass}, and the original password is {decoded_password}.\n")

        elif option == 3:
            break
