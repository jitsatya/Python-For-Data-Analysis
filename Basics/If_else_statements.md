
### If-else Statements in python


```python
# login prompt
correct_email = "satya@gmail.com"
correct_password = "1234"
email = input("Please enter your email: ")
password = input("Please enter your pasword: ")

if '@' in email:
    if email == correct_email and password == correct_password:
        print("welcome")
    elif email == correct_email and password != correct_password:
        print("password incorrect")
        password = input("Please enter correct pasword: ")
        if password == correct_password:
            print("Welcome")
        else:
            print("Too many incorrect attempt")
    else:
        print("Email invalid")
else:
    print("email invalid")
```

    Please enter your email: satya@gmail.com
    Please enter your pasword: 1234
    welcome

