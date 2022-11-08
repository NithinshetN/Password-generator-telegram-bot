import random
def random_generator(text,password):
    lower_case="abcdefghijklmnopqrstuvwzyz"
    upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="1234567890"
    symbols="!@#$%^&*()"

    string=lower_case+upper_case+numbers+symbols
    password_gen="".join(random.sample(string,password))
    
    return f"Account: '{text}'\npassword: {password_gen}"

