from datetime import datetime
import pytz

user_timezones = []

current_times = {
    '@Luke & @Jack': lambda t: datetime.now(pytz.timezone('Europe/Dublin')).strftime("%Y-%m-%d - %H:%M:%S"),
    '@Samnang': lambda t: datetime.now(pytz.timezone('Asia/Phnom_Penh')).strftime("%Y-%m-%d - %H:%M:%S"),
    '@Umut': lambda t: datetime.now(pytz.timezone('Europe/Istanbul')).strftime("%Y-%m-%d - %H:%M:%S"),
    '@Taproot': lambda t: datetime.now(pytz.timezone('America/Los_Angeles')).strftime("%Y-%m-%d - %H:%M:%S")
}

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

