def greet_day(day):
    day = day.lower()
    messages = {
        'monday': 'Happy Monday!',
        'tuesday': 'Terrific Tuesday!',
        'wednesday': 'Wonderful Wednesday!',
        'thursday': 'Thrilling Thursday!',
        'friday': 'Fantastic Friday!',
        'saturday': 'Super Saturday!',
        'sunday': 'Relaxing Sunday!'
    }
    if day in messages:
        return messages[day]
    else:
        return "no message."
user_day = input("Enter your  day of the week: ")
message = greet_day(user_day)
print(message)