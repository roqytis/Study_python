#연산자
from dask.array.ufunc import divmod
v1=3 #치환
v1=v2=v3=5
print(v1,v2,v3)
print('출력1', end = '')
print('출력2')

v1= 1, 2, 3
print(v1)
v1,v2= 10,20
print(v1, v2)
v2, v1= v1, v2
print(v1, v2)

print()
v1,*v2=1,2,3,4,5 #packing 연산
print(v1, v2)

print('성공')

*v1,v2=1,2,3,4,5 #packing 연산
print(v1, v2)
*v1,v2, v3=1,2,3,4,5 #packing 연산
print(v1, v2,v3)

print('----산술 연산 ------------------')
print(5+3, 5-3, 5*3,5/3)
print(5//3,5%3) #몫, 나머지
print(divmod(5,3))
print(5**2)

print('연산자 우선순위 :' , 3+4*5,(3+4)*5)

print('관계연산자------------------')
print(5>3, 5<=3, 5==3, 5!=3)
print('--논리 연산------')
print(5>3 and 4<3, 5>3 or 4<3, not(5>=3))

print('문자열 연산------------')
print('한'+"국인"+' 만세')
print('한국'+'한국'+'한국'+'한국')
print('한국'*5)

print('****'* 20)
print('누적')

a=10
a=a+1
a+=1
print(a)

print('부호변경')
print(a,a*-1,-a,+a,--a)

print('블린형')
print(True, False)
print(bool(1), bool(3.5), bool('ok'))
print(bool(0), bool(0.0), bool(' '), bool(None), bool({}),bool(set()))

print('이스케이프 문자')
print('aa\bb')
print('mbc\nbc')
print('c:\tbc\nbc')
print(r'aa\bb') #raw string
print(r'mbc\nbc')
print(r'c:\tbc\nbc')

print('\n출력 서식 연습')
print(1.5678)
print(format(1.5678,'10.3f'))

print('나는 나이가 %d 이다'%23)
print('나는 나이가 %s 이다'%'스물셋')
print('나는 나이가 %f 이다'%23.5)
print('나는 나이가 %d이고 이름은%s. 나이:%d '%(23,'홍길동', 23))
print()
print('이름은 {}, 나이는 {}'.format('이기자',25))
print('이름은 {0}, 나이는 {1}'.format('이기자',25))
print('이름은 {1}, 나이는 {0}'.format('이기자',25))
print('이름은 {0}, 나이는 {1} {0}'.format('이기자',25))
