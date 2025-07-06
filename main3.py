import datetime
#Get current date and time
now = datetime.datetime.now()
#Extract components
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")
hour = now.hour
minute = now.minute
second = now.second
year = now.year
print(f"{'Date':<20}{'Time':<20}{'Year':<10}")
print(f"{date:<20}{time:<20}{year:<10}")
print(f"{'Hour: ' + str(hour):<20}{'Minute: ' + str(minute):<20}{'Second: ' + str(second):<10}")