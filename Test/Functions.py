from functools import reduce

# Create the above functions without arguments
def emp_Id():
    print("12335")
emp_Id()
def emp_Name():
    print("Rajesh")
emp_Name()
def emp_Dob():
    print("12/06/1990")
emp_Dob()
def emp_Phone():
    print("987654321")
emp_Phone()
def emp_Email():
    print("raj1234@gmail.com")
emp_Email()
def emp_Address():
    print("OMR, Chennai")
emp_Address()

# Create the above functions with passing some arguments
print("\n")
def greens_Omr(Faculty, Address):
    print (Faculty, Address)
greens_Omr("Nitish,","Greens Tech,OMR, Chennai")
def greens_Adayar(Faculty, Address):
    print (Faculty, Address)
greens_Adayar("Anand,", "Greens Tech,Adayar, Chennai")
def greens_Tambaram(Faculty, Address):
    print (Faculty, Address)
greens_Tambaram('Bala,',"Greens Tech,Tambaram, Chennai")
def greens_Velacherry(Faculty, Address):
    print (Faculty, Address)
greens_Velacherry('Ganesh,',"Greens Tech,Velachery, Chennai")
def greens_Anna_Nagar(Faculty, Address):
    print (Faculty, Address)
greens_Anna_Nagar('Ashwin,',"Greens Tech,OMR, Chennai")

#Create the above function and pass two arguments and returntype of one value
print("\n")
def add(a, b):
    z = a+b
    return z
val = add(1,2)
print(val)
def sub(a, b):
    z = a - b
    return z
val = sub(1, 2)
print(val)

def calculator(a, b):
    sum = a+b
    sub = a-b
    mul = a*b
    div = a / b
    return sum, sub, mul, div
val = calculator(20, 20)
print(val)

''''def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Harry")'''

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def company_details(name, industry = 'IT', location='Chennai'):
    print('\nCompany name:',name,industry, location)
company_details("Britania")
def employee_details(name, id, location = 'Chennai'):
    print(name,id,location)
employee_details("Thaneesh", "12345")

def names(*name):
    return name
a = names("Arjun","Banu","Charlie")
print("\n",a)
def details(**details):
    return details
b = details(Empid = 12345, name = " Logan", Salary = 76543.23)
print(b)

'''def computer_names(*names):
  print(names)
computer_names(name1="hp",name2="sony",name3="dell")'''

def country_details(country_name,area_covered,country_population,no_of_states,no_of_unionterritories):
        print(country_name)
        print(area_covered)
        print(country_population)
        print(no_of_states)
        print(no_of_unionterritories)
country_details("\nIndia", "Asia", "1234567890", "28", "7")

# recursive function
c=0
def recursive():
    global c
    print("Welcome",c)
    c=c+1
    if c<=995:
        recursive()
recursive()

p=0
def recursive1():
    global p
    print("Python",p)
    p=p+1
    if p<=100:
        recursive1()
recursive1()

l1 = lambda a,b: a+b
l2 = lambda a,b: a-b
l3 = lambda a,b: a*b
print(l1(10, 20))
print(l2(10, 20))
print(l3(10, 20))

l4 = lambda n:n*n*n
print(l4(3))

h = int(input("Enter the value:"))
print(h)
l5=lambda h:h*h
print(l5(h))

#Filter
f = [1, 5, 4, 6, 8, 11, 3, 12]
def iseven(n):
    if n%2 ==0:
        return True
    else:
        return False
print(list(filter(iseven, f)))

#Map
m = [2, 4, 8, 11, 24, 10, 3, 27]
def double(j):
    return j*2
print(list(map(double, m)))

#reduce
def add(a,b):
    return a+b
re = [1,2,4,3]
print(reduce (add, re))

def mul(x,y):
    return x*y
r1 = [2,6,11,24,27]
print(reduce (mul, r1))
