from datetime import datetime


def clientime() -> str:
    now = datetime.now()
    current_time = now.hour
    return current_time


def greet() -> str:
    if clientime() < 12:
        greeting = 'Good Morning'
        return greeting
    elif 12 <= clientime() < 18:
        greeting = 'Good Afternoon'
        return greeting
    else:
        greeting = 'Good Evening'
        return greeting
