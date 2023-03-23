# Angely Gomez
def password_encoder(password):
    encoded_pass = ""
    for number in password:
        encoded_pass += password_encoder_dict(number)
    return encoded_pass


def password_encoder_dict(password):
    encoded = {'0':'3', '1':'4', '2':'5', '3':'6', '4':'7', '5':'8', '6':'9', '7':'0', '8':'1', '9':'2'}
    return encoded[password]


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
            pass

        elif option == 3:
            break
