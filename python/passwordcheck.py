username = input('What is your name\n')
user_lname = input('Enter your last name\n')
password = input('What is your password\n')

password_lenth =len(password)
hidden_pasword ='*'* password_lenth

print(f'''
Your name is {username} {user_lname}
Your password is {hidden_pasword}
lenth of password {len(password)}
''')