def msg():
    print("Welcome to python class")
msg()

name = input("Enter your name:")
age = input("Enter you age:")
address = input("Please enter your address:")
def details(name, age):
    print("Application form submitted for: ", name, age)
details(name, age)

def addr(address):
    return address
a = addr(address)
print(a)
