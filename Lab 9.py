def encode(password):
    newPassword = []
    for char in password:
        newChar = (int(char) + 3)%10
        newPassword.append(str(newChar))
    return "".join(newPassword)


def main():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    option = input("Please enter an option:")

    if option == 1:
        password = input("Please enter the password to encode: ")
        print(encode(password))
    if option == 2:
        password = input("Please enter the password to decode: ")
