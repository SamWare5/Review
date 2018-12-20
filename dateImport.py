import datetime

x = datetime.datetime.now()

print(x)

print(x.year)
print(x.strftime("%A"))

date_to_print = ""
date_to_print = x.strftime("%Y-%m").lower()
print(x.strftime("%Y-%m"))
print(date_to_print)
print(x.strftime("%Y-%m-%d %I:%M%p").lower())


print("x", 10)