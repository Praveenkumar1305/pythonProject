list_a=[1,2,3,5,6,7,5,2]

tmp=[]

for i in list_a:
    if tmp.__contains__(i):
        print(i)
    else:
        tmp.append(i)