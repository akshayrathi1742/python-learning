username = input(
    'what is your username\n'
    )
password = input(
    'what is your password\n'
    )
password_lenth = len(password)
hidden_password = '*'*password_lenth


print(
    f' Your Name {username}\n Your password {hidden_password}: {len(password)}'
     )