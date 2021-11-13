# Write Python program to allow the user to input his/her age.
# Then the program will show if the person is eligible to vote.
# A person who is eligible to vote must be older than or equal 1 to 18 years old.

x = input("Enter your name:")
a = int(input("Please enter your age:"))

if (a>=18):
    print("\n", x)
    print("You are Eligible to vote")
else:
    print("\n", x)
    print("You are not Eligible to vote")

# Write a program to find even or odd number

y = int(input("Enter a value:"))
z = y % 2
print(z)
if (z==0):
    print('even')
else:
    print('odd')

# Write a program to print even number from 1 to 100

for i in range(1, 100):
    z = i % 2
    if (z == 0):
        print(i)

# Find the sum of even number 1 to 100

j=0
for i in range(1, 100):
    z = i % 2
    if (z == 0):
        j = i+j
print(j)


# Find the sum of odd number 1 to 100

j=0
for i in range(1, 100):
    z = i % 2
    if (z != 0):
        j = i+j
print(j)

# Count of even numbers

j=0
for i in range(1, 100):
    z = i % 2
    if (z == 0):
        j+=1

print(j)


# Count of odd numbers

a=0
for x in range(1, 100):
    b = x%2
    if (b!=0):
        a+=1
print(a)
