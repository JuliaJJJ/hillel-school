value = int(input("Enter number: "))

sec_per_day = 24 * 60 * 60
sec_per_hour = 60 * 60
sec_per_min = 60

day = value // sec_per_day
hour = (value % sec_per_day) // sec_per_hour
minute = (value % sec_per_hour) // sec_per_min
second = value % sec_per_min

last10 = day % 10
last100 = day % 100

if last10 == 1 and last100 != 11:
    day_string = "день"
elif 2 <= last10 <= 4 and not (12 <= last100 <= 14):
    day_string = "дні"
else:
    day_string = "днів"

hh = str(hour).zfill(2)
mm = str(minute).zfill(2)
ss = str(second).zfill(2)

print(f"{day} {day_string}, {hh}:{mm}:{ss}")