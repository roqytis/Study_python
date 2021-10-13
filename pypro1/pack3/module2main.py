#사용자가 만든 모듈 일기
print('이건 메인 모듈')

print('같은 패키지 내의 모듈 호춣하기')
import pack3.mymod1
print('tot : ', pack3.mymod1.tot)

aa=1,2,3
bb=(4,5)
pack3.mymod1.listTotal(aa,bb)
'''
def abc():
     if __name__=='__name__':
         print('메인이야')
abc()
'''
def abc():
    print('abc 함수')
    
if __name__=='__main__':
    abc()
    
print()
from pack3.mymod1 import kbs, mbc
kbs()
mbc()

print('다른 패키지 내의 모듈 호출하기--------')
import pack3other.mymod2
print(pack3other.mymod2.hap(5, 3))
from pack3other.mymod2 import cha
print(cha(5,3))

print('파이썬이 제공하는 그래픽 모듈 도형 그리기')
import turtle
'''
a= turtle.Pen()
a.forward(100)
a.right(90)
a.forward(100)
a.right(90)
a.forward(100)
a.right(90)
a.forward(100)
turtle.done
input()
'''
from turtle import *
p=Pen()
p.color('red', 'yellow')
p.begin_fill()
while True:
    p.forward(200)
    p.left(170)
    if abs(p.pos()) < 1:
        break
p.end_fill()
done()
p.end_fill()