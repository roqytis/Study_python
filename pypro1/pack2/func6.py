# 파이썬은 일급함수를 지원
# 함수 안에 함수 선언 가능, 인자로 함수 전달, 반환값으로 함수가 가능


def func1(a, b):
    return a+b

func2 = func1
print(func1(2,3))
print(func2(2,3))
print()
def func3(func):
    def func4():
        print('나는 내부 함수야~~')
    func4()
    return func

mbc= func3(func1)
print(mbc(3,4))

print('축약함수(lambda- 이름이 없는 한 줄 짜리 함수)')
#형식- lambda 인제,,,; 표현식
def hap(x, y):
    return x+y
print(hap(2,3))

print('위 소스를 람다로 표현')
print((lambda x,y: x+y)(2,3))

gg= lambda x,y: (x+y)*2
print(gg) #<function <lambda> at 0x000002B4BE2DD3A0>
print(gg(3,4))

print()
kbs = lambda a, su =10:a + su
print(kbs(9))
print(kbs(9,2))

print()
sbs =lambda a,*tu,**di : print(a,tu,di)
sbs(1,2,3,mbc=11,kbs=9)

print()
li =[lambda a,b:a+b, lambda a,b:a*b, lambda:7]
print(li[0](3,4))
print(li[1](3,4))
print(li[2]())

print('함수 인자로 람다를 사용하기')
#filter(함수,sequence자료)
print(list(filter(lambda a:a<5, range(10))))
print(list(filter(lambda a:a%2, range(10))))