#length
s = {10,20,30,90,10,10,40,50}
print(len(s))

s1 = {100,200,300,400,500,600,700}
print(len(s1))

s2 = {'python','selenium','sql','java'}
print(len(s2))

s3 = {10,20,30,90,10,10,40,50,'python','java',22.4,'True'}
print(len(s2))
print('----------------')

#index - Set has no attribute as index

#max - mini
a = {10,20,30,90,10,10,40,50,10 }
print(max(a))

a1= {'python','selenium','sql','java'}
print(min(a1))

a2 = {100,200,300,900,400,500,1000}
print(min(a2))

a3 = {'python','selenium','sql','java'}
print(min(a3))
print('----------------------')

#update
u = {10,20,30,40,50,60}
u.update({100,200, 500})
print(u)

u1 = {100,200,300,400,500,600,700}
u1.update(['java','sql'])
print(u1)

u2 = {105,205,305,405,505,605,705,805}
u2.update(['greens'])
print(u2)

u3 = {105,205,305,405,505,605,705,805}
u3.update((100,200,500))
print(u3)

u4 = {105,205,305,405,505,605,705,805}
u4.update(('j'+'greens'))
print(u4)
print('--------------------------')

#Convert
c= 'python'
print(set(c))

c1 = ['java','python',20,10,60]
print(set(c1))

c2 = (105,205,305,405,505,605,705,805,'java','python',20,10,60)
print(set(c2))
print('------------------')

# Check
c3 = { 105,205,305,405,505,605,705,805}
print(200 in c3)
print(200 not in c3)
print(505 in c3)
print(505 not in c3)
print('------------------------')

#compare
set= {10,20,30,40,50,60}
set1 = {10,20,30,40,50,60}
print(set==set1)

c4 = {10,20,30,40,50,60}
c5 = { 60,20,30,40,50,10}
print(c4==c5)

#for
s ={ 105,205,305,405,505,605,705,805}
for i in s:
    print(i)
print('-------')
for j in enumerate(s):
    print(j)
print('------------')
for k,l in enumerate(s):
    if k % 2 !=0:
        print(k, l)
print('----------------')

#union, intersection, difference, symetric diff.
un = {10,20,30,40,50,60}
un1 = { 60,80,90,40,50,10}
print(un.union(un1))
print(un.intersection(un1))
print(un.difference(un1))
print(un.symmetric_difference(un1))

