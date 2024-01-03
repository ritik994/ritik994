import datetime
def greet_user(name):
    current_time = datetime.datetime.now()
    if 6 <= current_time.hour < 12:
        greeting = "Good morning"
    elif 12 <= current_time.hour < 18:
        greeting = "Good afternoon"
    elif 18 <= current_time.hour < 24:
        greeting = "Good evening"
    else:
        greeting = "Hello"
    return f"{greeting}, {name}!"


my_name = "Ritik"
greeting_message = greet_user(my_name)


print(greeting_message)