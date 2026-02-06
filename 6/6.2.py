seconds = int(input("Введіть кількість секунд: "))

seconds_in_day = 24 * 60 * 60
seconds_in_hour = 60 * 60
seconds_in_minute = 60

days = seconds // seconds_in_day
seconds = seconds % seconds_in_day

hours = seconds // seconds_in_hour
seconds = seconds % seconds_in_hour

minutes = seconds // seconds_in_minute
seconds = seconds % seconds_in_minute

if days == 1:
    day_word = "день"
elif 2 <= days <= 4:
    day_word = "дні"
else:
    day_word = "днів"

print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
