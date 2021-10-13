#반복문 while문


a = 1
while a<= 5:
    print(a, end=' ')
    a +=1
    
    print('탈출 후 a: ',a)
    
print()
i=1
while i <=3:
    j=1
    while j<= 4:
        print('i:'+ str(i)+', j:'+str(j))
        j=j+1
    i=i+1
    
print('1~100 사이의 점수 중 3의 배수의 합 출력')
i= 1; hap= 0; count =0
while i<=100:
    if i%3==0:
        #print(i, end=' ')
        hap +=i
        count +=1
    i +=1
print('합은: ',hap)
print('건수: ',count)

print()
colors = ['red','green','blue','yellow','black']
print(colors)
index =0
while index < len(colors):
    print(colors[index], end=' ')
    index= index+1

print()
#print(colors.pop())
#print(colors.pop())
print('수정전: ', len(colors))
while colors:
    print(colors.pop())
    
print('수행후: ', len(colors))    

print('별 찍기')
i=1
while i<=10:
    j=1
    str=''
    while j<=i:
        str=str+'*'
        j=j+1
    print(str)
    i=i+1
'''   
# 폭탄 터뜨리기
import time
print(time.localtime().tm_year)
time.sleep(3)
print('종료')
'''
import time

sw= input('폭탄 스위치를 누를까요[y/n]')
if sw == 'Y' or sw == 'y':
    count = 5
    while 1<= count:
        print('%d초 남았어요'%count)
        time.sleep(1)
        count -= 1
    print('폭발')
elif sw == 'N' or sw== 'n':
    print('작업취소')
else:
    print('y 또는 n을 누르시오')        
