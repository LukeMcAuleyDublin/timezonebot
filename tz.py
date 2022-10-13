from datetime import datetime
import pytz
import csv

current_times = {
    'America/New_York': lambda t: datetime.now(pytz.timezone(t)).strftime("%Y-%m-%d - %H:%M:%S"),
    'Europe/Dublin': lambda t: datetime.now(pytz.timezone(t)).strftime("%Y-%m-%d - %H:%M:%S"),
    'Asia/Phnom_Penh': lambda t: datetime.now(pytz.timezone(t)).strftime("%Y-%m-%d - %H:%M:%S"),
}

def timezones():
    string_to_send = ""
    for k, v in current_times.items():
        print(f"{k}: {v(k)}")
        string_to_send += f"```\n{k}: {v(k)}\n```"
    return string_to_send

# with open("timezones.csv", "w") as f:
#     csvwriter = csv.writer(f)
#     csvwriter.writerow(pytz.all_timezones)
