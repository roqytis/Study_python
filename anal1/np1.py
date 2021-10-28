# numpy module

grades = [1,3,-2,4]

def grades_var(grades):
    tot =0
    for g in grades:
        tot += g
    ave= tot/len(grades)
    vari = 0
    for su in grades:
        vari +=(su-ave)**2
    return vari/len(grades)

print("분산 값 : ",grades_var(grades))

import numpy

print("분산 값 : ",numpy.var(grades))
print("표준편차 값 : ",numpy.std(grades))

import numpy as np
ss = ['tom', 'james', 'john']
print(ss, type(ss)) #class list

ss2= np.array(ss)
print(ss2,type(ss2)) #<class 'numpy.ndarray'>

# list vs ndarray
li = list(range(1,10))
print(li)
print(id(li[0]), id(li[1])) #140706975852336 140706975852368
print(li * 10)
print([i * 10 for i in li])
print('--'* 10)

num_arr = np.array(li)
print(id(num_arr[0]),id(num_arr[1]))#1959362199440 1959362199440
print(num_arr * 10)

print()
a= np.array([1,2,3])
print(a,' ',type(a),' ',a.dtype,' ',a.shape,' ',a.ndim,' ',a.size)
print(a[0],a[1],a[2])

print()
b=np.array([[1,2,3],[4,5,6]])
print(b.shape) #(2, 3)
print(b[0,0],b[1,1]) #1 5
print(b[0],' ',b[0])

print()
c = np.zeros((2,2))
print(c)

d = np.ones((1,2))
print(d)

e = np.full((2,3),7)
print(e)

f = np.eye(3)
print(f)

print()
x1 = np.random.randint(10, size=6)
print(x1)

x2 = np.random.randint(10, size=(3,4))
print(x2)

x3 = np.random.randint(10, size=(2,3,4))
print(x3)

print('----------')
a = np.array([1,2,3,4,5])
print(a[1:5:2])

a= np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a[:])
print(a[0],a[0][0], a[[0]])
print(a[[0][0]],a[0,0])
print(a[1:, 0:2])

b= a[:2,1:3] # sub array
print(b)
print(b[0,0])
b[0,0]=77

print(b)
print()
print(a)

print()
bool_idx= (a> 10)
print(bool_idx)
print(a[bool_idx])
print(a[a >= 10])