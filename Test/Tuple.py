#length
l = (10,20,30,90,10,10,40,50)
print(len(l))

l1 = (100,200,300,400,500,600,700)
print(len(l1))

l3 = ('python','selenium','sql','java')
print(len(l3))

l4 = (10,20,30,90,10,10,40,50,'python','java',22.4,'True')
print(len(l4))
print('-----------------')

#index
i = (10,20,30,90,10,10,40,50)
print(i.index(10))
print(i. index(10,5))
print(i.index(50))
#print(i.index(200))
print('--------------------')

#slice
s= (10,20,30,40,50,60)
print(s[2])
s1 = (100,200,300,400,500,600,700)
print(s1[4])
s2 = (105,205,305,405,505,605,705,805)
#print(s2[12])
print(s2[-3])
print(s2[-8])
print('-------------------')

#add - Tuple is unmodifiable

#Count
c = (10,20,30,90,10,10,40,50,10)
print(c.count(10))
print('-----------------')

#max, min
print(max(c))
print(min(c))

m = ('python','selenium','sql','java')
print(max(m))
print(min(m))
print('---------------------')

#convert
c1 = "python"
print(tuple(c1))

List = ['java','python',20,10,60]
print(tuple(List))
print('-----------------------------')

#check
tuple = (105,205,305,405,505,605,705,805)
print(200 in tuple)
print(200 not in tuple)
print(505 in tuple)
print(505 not in tuple)
print('----------------------------')

#compare
t = (10,20,30,40,50,60)
t1 = (10,20,30,40,50,60)
t2 = (60,20,30,40,50,10)
print(t == t1)
print(t==t2)
print('-----------------------------')

#for
f = (105,205,305,405,505,605,705,805)
for j in f:
    print(j)
print('--------------------------------------')
for e in enumerate (f):
    print(e)
print('------------------------------')
for ind,val in enumerate (f):
    if ind % 2 ==0:
        print(ind, val)
