#변수의 생존 범위 (scope rule)
#접근순서 ㅣ local >Enclosing funtion > Global

player ='전국대표' #전역변수

def funcSoccer():
    name ='신기해'
    player='조기축구 대표'
    print(name, player)
    
aa = funcSoccer #함수의 주소 치환
print(aa)
aa2 = funcSoccer() #함수의 수행 결과를 치환
print(aa2)

print('------')
funcSoccer()

#print(name) #name 'name' is not defined
print(player)

print('****'*10)
a=10; b=20; c=30
print('처리1=>  a:{}, b:{}, c:{}'.format(a,b,c))
def foo():
    a=40
    b=50
    def bar(): #함수 내에 함수 선언
        #c=60
        global c #전역변수로 사용
        nonlocal b
        print('처리2=>  a:{}, b:{}, c:{}'.format(a,b,c)) #UnboundLocalError: local variable 'c' referenced before assignment
        c=60 #UnboundLocalError: local variable 'c' referenced before assignment
        b=70
    bar()
    print('처리4=>  a:{}, b:{}, c:{}'.format(a,b,c))
    
foo()
print('처리4=>  a:{}, b:{}, c:{}'.format(a,b,c))


        