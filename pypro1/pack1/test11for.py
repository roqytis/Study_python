# range 함수 : 수열 생성
print(list(range(1,6)))
print(list(range(6)))
print(list(range(1,6,1)))
print(list(range(1,6,2)))
print(tuple(range(1,6)))
print(set(range(1,6)))

print()
for i in range(6):
    print(i,end=' ')
    
print()
for _ in range(6):
    print('hi',end=' ')
    
print('\n1~10까지의 합')
tot=0
for i in range(1,11):
    tot+=i
print('합계는: ',tot)
print('결과는', sum(range(1,11)))

print()
for i in range(2,10,2):
    for j in range(1, 10):
        print('{}*{}={}'.format(i,j,i*j), end=' ')
    print()
    
# 문1) 반복문 for을 이용: 1~100사이의 정수 중 3의 배수이면서 5의 배수의 합, 건수 출력
tot = 0
cou = 0
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
       #print(i)
        tot += i
        cou += 1
print('합계 =' , tot , '건수 :', cou)


# 문2) 주사위를 두 번 던져서 숫자들의 합이 4의 배수가 되는 경우만 출력 
for i in range(1, 7):
    for j in range(1, 7):
        if (i + j) % 4 == 0:
          print(i, ' ', j)  
print()

print()
for i in range(6):
    n1=i+1
    for j in range(6):
        n2= j+1
        n= n1+n2
        if n%4==0:
            print(n1,' ',n2)
