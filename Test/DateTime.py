import datetime

dt = datetime.datetime.now()
print(dt)

print("Year")
print(dt.strftime("%Y"))
print(dt.strftime("%y"))

print("Month")
print(dt.strftime("%B"))
print(dt.strftime("%b"))

print("Date")
print(dt.strftime("%A"))
print(dt.strftime("%a"))

print(dt.strftime("%Y-%B-%A"))