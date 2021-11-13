# Find the length of the below string

s1 = 'GreensTechnology'
i = len(s1)
print("GreensTechnology:\t", i)

s2 = 'Python Programming'
print('Python Programming:\t', len(s2))

s3 = 's e l e n i u m'
print('s e l e n i u m:\t', len(s3))

s4 = '9876543210'
print('9876543210:\t', len(s4))

s5 = 'Hi welcome to the world of programs'
print('Hi welcome to the world of programs:\t', len(s5))

# Find the index position
#  Find the index of e
s1 = 'Greens Technology'
i = s1.index('e')
j = s1.rindex('e')
print('\n The index of e:')
print('Greens Technology:\t', i)
print('Greens Technology:\t', j)

# Find the index of testing
s2 = 'Automation testing tool'
print('\n The index of testing:')
print('Testing:\t', s2.index('testing'))

# Find the index of automation and using
s3 = 'Selenium automation using Python'
print('\n The index of automation & testing:')
print('Automation:\t', s3.index('automation'))
print('Using:\t', s3.index('using'))

# Find the index of c, Java, Ruby, q and t
s4 = 'Programming languages are c,c++,Java and Python'
print('\n The index of c, Java, Ruby, q and t:')
print(s4.find('c'))
print(s4.find('Java'))
print(s4.find('Ruby')) # Facing error for finding the index for unknown word
print(s4.find('q'),"&", s4.find('t')) # Facing error for finding the index for unknown character

# Using Find method perform the below operations

s1 = 'Selenium automation using Python'
print('1st Occurence of automation:\t', s1.find('automation'))
print('1st Occurence of Python:\t\t', s1.find('Python'))

# Given String is "Welcome to Python class" and find the substring

Input = "Welcome to Python class"
print(Input[1])
print(Input[1:5])
print(Input[8:10])
print(Input[11:17])
print(Input[8:])

# And also try with negative scenarios

Input1 = "Welcome to Python class"
print("\n")
print(Input1[-17])
print(Input1[-22:-18])
print(Input1[-15:-13])
print(Input1[-12:-6])
print(Input1[-15:])

# Find whether the string python is present or not, using 'if'

Input = 'Programming languages are c,c++,Java and Python'

if(Input.find('Python') != -1):

    print("Contains substring 'Python'")

else:

    print("Doesn't contain substring")

# Given String as "Welcome to Python class" and split it by space

Input = 'Welcome to Python class'
i = Input.split(' ')
for i in i:
    print('split it by space:\t', i)
print("\n")
j = Input.split('l')
for j in j:
    print('split it by l:\t', j)

# Find the count of word "is"

Input = 'Python is awesome and it is dynamic language'
i = Input.count('is')
print('Count of "is"\t:', i)

# Find the count of character 'm'

Input = "Java programming and Python programming"
print('Count of "m" \t:', Input.count('m'))

# Get the input from the user and find the count of character 'o'

x = "Hi welcome to the world of programs"
i = input("Please enter letter to count:")
print(x.count(i))

# Get two input strings from user and Compare

s1 = input("Enter the string1:")
s2 = input("Enter the string2:")
print("Compare:\t\t", s1==s2)

# Given String as "Welcome to Python class" and verify whether the given string startsWith welcome

Input  = 'Welcome to Python class'
i = Input.startswith('Welcome')
j = Input.endswith('class')
print(i)
print(j)

Input1  = 'Hai I am from Greens'
print(Input1.startswith('Welcome'))
print(Input1.endswith('Python'))

# Get the input from the user and print that word in lowercase

i = input('Enter the string in upper case:')
l = i.lower()
print('Changed to lower:\t',l)

# Get the input from the user and print that word in Uppercase

j = input('Enter the string in lower case:')
u = j.upper()
print('Changed to upper:\t',u)

# Get the input from the user and print the first letter in capital

k = input('Enter the string:')
c = k.capitalize()
print('Changed 1st letter to capital:\t',c)

# Remove the unwanted spaces from the given string

Input = "      Incredible India        "
s = Input.strip()
print(s)

# Remove the left side spaces from the given string

Input1 = "      Software Engineering        "
l = Input1.lstrip()
print(l)

# Remove the right side spaces from the given string

Input2 = "     Dynamic language        "
r = Input2.rstrip()
print(r)


