from datetime import datetime
import pytz

user_timezones = []

current_times = {}

def timezones():
    string_to_send = "```"
    for k, v in current_times.items():
        print(f"{k}: {v(k)}")
        string_to_send += f"\n{k}: {v(k)}\n"
    string_to_send += '```'
    return string_to_send

def timezone_in_list(tz):
    with open('timezones.txt', 'r') as f:
        for line in f:
            if tz in line:
                return True
    return False

def add_timezone(tz):
    if timezone_in_list(str(pytz.timezone(tz))) == False:
        user_timezones.append(tz)

def populate_current_times():
    for tz in user_timezones:
        current_times[tz] = lambda t: datetime.now(pytz.timezone(t)).strftime("%Y-%m-%d - %H:%M:%S")

add_timezone('Asia/Tokyo')
add_timezone('Europe/Dublin')

populate_current_times()

print(user_timezones)
print(timezones())

