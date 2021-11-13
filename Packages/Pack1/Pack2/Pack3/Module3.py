from functools import reduce

fmr = [1,2,3,4,5,6,7,8,9]
def is_odd(n):
    if n%2 !=0:
        return True
    else:
        return False
print("Odd no's are:",list(filter(is_odd, fmr)))

print("Even no's are:",list(filter(lambda n: n%2 ==0, fmr)))

def cube(n):
    return n*n*n
print("Cube:", (list(map(cube, fmr))))

def con(a,b):
    return a+b
print(reduce(con, fmr))


