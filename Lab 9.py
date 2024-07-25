def encode(password):
    newPassword = []
    for char in password:
        newChar = (int(char) + 3) % 10
        newPassword.append(str(newChar))
    return "".join(newPassword)
