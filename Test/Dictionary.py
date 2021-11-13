#length
l = {100:'java',200: 'sql',300:'oops',400:'sql',500:'oracle',600:'DB',100:'selenium',500:'psql',400:'Hadoop'}
print(len(l))

l1 = {'a': 10,'b': 20,'c':30,'d': 40,'e':50}
print(len(l1))

l2 = {90:11.50,60:20.50,40: 55.00,20:88.90,55:33.30,70:66.00,30:99.99}
print(len(l2))

l3= {'vel':'Selenium','Ganesh':'framework','Dinesh':'oracle','Vengat':'python','subash':'jira'}
print(len(l3))
print('---------------------------')

#get

g = l1.get('b')
print(g)
g1 = l3.get('vel')
print(g1)

g3 = {10:10+10j,20:20+2j,30:30+3j,40:40+4j,50:50+5j,60:60+6j,10:10+10j,50:50+5j,40:40+4j}
get = g3.get(50)
print(get)
print('---------------------------')

#iterate - keys & vales
i = {10:101,20:202,30:303,40:404,50:505,60:606,10:101,50:505,40:404}
k = i.keys()
for j in k:
    print('keys:',j)
v = i. values()
for j1 in v:
    print('values:',j1)
print('------')
i1 ={'vel':'Selenium','Ganesh':'framework','Dinesh':'oracle','Vengat':'python','subash':'jira'}
k1 = i1.keys()
v1 = i1.values()
print(k1, "\n",v1)
print('-------')
gg = {10:10+10j,20:20+2j,30:30+3j,40:40+4j,50:50+5j,60:60+6j,10:10+10j,50:50+5j,40:40+4j}
g4 = gg.keys()
g5 = gg.values()
g6 = gg.items()
for n,ma in g6:
    print(n,ma)
print('----------------')
#Remove
r = {10:100, 20:200, 30:300, 40:400, 50:500, 60:600}
r.pop(50)
print(r)

r1 = {10.9:'python', 20.1:'selenium'  ,30.2:'java',40.3:'c',50.4:'c++',60.5:'oracle'}
r1.pop(10.9)
print(r1)

r2 = {'Tamil':'TamilNadu','English':'Uttar Pradesh','Malaiyalam':'Kerala','Telugu':'Telangana','Kanadam':'Karnataka','Hindi':'Delhi'}
r2.pop('Malaiyalam')
print(r2)
print('--------------')

#slice
r[70] = 900
print(r)

r2['Hindi']= 'Mumbai'
print(r2)
print('----------------')

#convert

l = [10,'vel','vel@gmail.com'],[20,'nisha','nisha@gmail.com'],[30,'bala','bala@gmail.com']
print(list(l))
l1 = (10,'vel','vel@gmail.com'),(20,'nisha','nisha@gmail.com'),(30,'bala','bala@gmail.com')
print(list(l1))
l2 = {10,'vel','vel@gmail.com'},{20,'nisha','nisha@gmail.com'},{30,'bala','bala@gmail.com'}
print(list(l2))
l3 = {'id':10,'name':'vel','email':'vel@gmail.com'},{'id':20,'name':'nisha','email':'nisha@gmail.com'},{'id':30,'name':'bala','email':'bala@gmail.com'}
print(list(l3))
print('-----------------------------')
t =[10,'vel','vel@gmail.com'],[20,'nisha','nisha@gmail.com'],[30,'bala','bala@gmail.com']
print(tuple(t))
t1 = (10,'vel','vel@gmail.com'),(20,'nisha','nisha@gmail.com'),(30,'bala','bala@gmail.com')
print(tuple(t1))
t2 = {10,'vel','vel@gmail.com'},{20,'nisha','nisha@gmail.com'},{30,'bala','bala@gmail.com'}
print(tuple(t2))
t3 = {'id':10,'name':'vel','email':'vel@gmail.com'},{'id':20,'name':'nisha','email':'nisha@gmail.com'},{'id':30,'name':'bala','email':'bala@gmail.com'}
print(tuple(t3))