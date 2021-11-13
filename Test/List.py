# List

l = [10, 20, 30, 90, 10, 10, 40, 50]
print(len(l))

l1 = [105, 205, 305, 405, 505, 605, 705, 805]
print(len(l1))

l2 = ['Java', 'Python', 'Selenium', 'java', 10, 20, 10]
print(len(l2))

# Get the  index value of 10

l3 = [10, 20, 30, 90, 10, 10, 40, 50]
i = l3.index(10)
print(i)

l4 = [10, 20, 30, 90, 10, 10, 40, 50]
j = l4.index(10, 5)
print(j)

l5 = [10, 20, 30, 90, 10, 10, 40, 50]
k = l5.index(50)
print(k)

l6 = [10, 20, 30, 90, 10, 10, 40, 50]
a = l6.index(90)
print(a)

''''l7 = [10,20,30,90,10,10,40,50,10]
b = l7.index(70)
print(b)'''''

l8 = [10, 20, 30, 90, 10, 10, 40, 50]
l8.append([100, 200, 300])
print(l8)

l9 = [10, 20, 30, 90, 10, 10, 40, 50, 100, 200, 300]
l9.extend([100, 200, 300])
print(l9)
g = l9.index(200)
print(g)

u = [10, 20, 30, 40, 50, 60]
print(u[2])

u1 = [100, 200, 300, 400, 500, 600, 700]
print(u1[4])

u2 = [105, 205, 305, 405, 505, 605, 705, 805]
print(u2[-2])

''''u3 = [105,205,305,405,505,605,705,805]
print(u3[-10])'''''

q = [10, 20, 30, 40, 50, 60]
print(q.pop(2))
print(q)

'''p =[10,20,30,90,10,10,40]
print(p.pop(10))'''

s = [10, 20, 30, 90, 10, 10, 40]
del s[-2]
print(s)

s1 = [10, 20, 30, 90, 10, 10, 40]
s1.pop()
print(s1)

s2 = [10, 20, 30, 90, 10, 10, 40, 60, 80, 100]
s2.remove(80)
print(s2)

''''s3 = [10,20,30,90,10,10,40,60,80,100]
s3.remove(50)
print(s3)'''''

s4 = [10, 20, 30, 90, 10, 10, 40, 60, 80, 100]
del s4[-5: -1]
print(s4)

s5 = [10, 20, 30, 90, 10, 10, 40, 60, 80, 100]
del s5[2:]
print(s5)

s6 = [10, 20, 30, 90, 10, 10, 40, 60, 80, 100]
s6.clear()
print(s6)

r = [100, 200, 300, 400, 500, 600, 700]
r[2] = 350
print(r)

r1 = [10, 20, 30, 90, 10, 10, 40, 50, 10]
r1[7] = 90
print(r1)

r2 = [10, 20, 30, 90, 10, 10, 40, 50]
r2.insert(2, 50)
print(r2)

r3 = [10, 20, 30, 90, 10, 10, 40, 50]
r3.append(70)
print(r3)

r4 = [10, 20, 30, 90, 10, 10, 40, 50]
r4.insert(30, 80)
print(r4)

r5 = [10, 20, 30, 90, 10, 10, 40, 50]
r5.insert(-2, 100)
print(r5)

r6 = [10, 20, 30, 90, 10, 10, 40, 50]
r6.append([100, 200, 300])
print(r6)

r7 = [10, 20, 30, 90, 10, 10, 40, 50]
r7.extend([100, 200, 300])
print(r7)

r8 = [10, 20, 30, 90, 10, 10, 40, 50]
h = r8.count(10)
print(h)

r9 = [10, 20, 30, 90, 10, 10, 40, 50]
print(max(r9))

r10 = ['java', 'python', 'selenium', 'Java', 'Python', 'Selenium']
print(max(r10))

r11 = [10, 20, 30, 90, 10, 10, 40, 50]
print(min(r11))

r12 = ['java', 'python', 'selenium', 'Java', 'Python', 'Selenium']
print(min(r12))

d = [10, 20, 30, 50, 90, 40, 100, 60, 10, 70]
d.reverse()
print(d)

d1 = [10, 20, 30, 50, 90, 40, 100, 60, 10, 70]
v = sorted(d1)
print(v)
v.reverse()
print(v)

d2 = [10, 20, 30, 90, 10, 10, 40, 50]
d2.copy()
print(d2)

n = [10, 20, 30, 90, 10, 10, 40, 50]
n1 = [30, 40, 50, 60, 80]

print(n == n1)

n2 = [10, 20, 30, 90, 10, 10, 40, 50]
n3 = [10, 20, 30, 90, 10, 10, 40, 50]

print(n2 == n3)

n4 = [105, 205, 305, 405, 505, 605, 705, 805]
for v1 in n4:
    print(v1)

n5 = [105, 205, 305, 405, 505, 605, 705, 805]
for v2 in enumerate(n5):
    print(v2)

print('----------------')

n6 = [105, 205, 305, 405, 505, 605, 705, 805]
for v13, v14 in enumerate(n6):
    if (v13 % 2) != 0:
        print(v13, v14)
