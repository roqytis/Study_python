'''
여러 줄
주석
'''
# 한 줄 주석
var1='안녕 파이썬!'
print(var1)
var1=3; print(var1)

a=10
print(a,'',id(a),'',type(a))

b=10.5
print(b,'',id(a),'',type(b))

c="python"
print(c,'',id(c),'',type(c))

d= True
print(d,'',id(d),'',type(d))

A=10
a=10
b=10
print('주소비교:',a==b,',값 비교:',a is b)

print('-----------------------')
print(10,'',oct(10),'',hex(10),'',bin(10)) #10  0o12  0xa  0b1010
print(10,  0o12,  0xa,  0b1010)
print('\n-----------------------')
print(3,type(3))
print(3.1,type(3.1))
print(3+4j,type(3+4j))
print(False,type(False))
print('a',type('a'))

print()
#묶음형 자료형
print((1,),type((1,)))
print([1],type([1]))
print({1},type({1}))
print({'key':1}, type({'key':1}))



