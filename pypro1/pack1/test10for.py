#반복문 for
for i in [1,2,3,4,5]:
    print(i, end=' ')
    
print()

#colors= ['r','g', 'b']
#colors= ('r','g', 'b')
colors= {'r','g', 'b'}
for c in colors:
    print('색은%s'%c, end=' ')
    
print()
soft = {'java':'웹용 언어', 'python':'만능언어', 'c':'시스템개발용'}
for i in soft.items():
    #print(i) #('java', '웹용 언어')....
    print(i[0]+' '+i[1])
    
print()
for k in soft.keys():
    print(k, end=" ")
    
print()
for v in soft.values():
    print(v,end=' ')
    
print()
for a,b in soft.items():
    print(a,', ',b) 
    
print('평균, 분산, 표준편차')
jum=[6,5,4,7,3.5]
tot=0
for i in jum:
    tot +=i
    
avg=tot/len(jum)
print('avg=',avg)

tot =0
for i in jum:
    tot +=(i-avg)**2
var =tot/len(jum)
print('var :',var)
import math
print('std: ', math.sqrt(var))

print()
for n in [2,3]:
    print('----{}단----'.format(n))
    for su in [1,2,3,4,5,6,7,8,9]:
        print('{}*{}={}'.format(n,su,n*su))
        
print()
li =['a','b','c']
for idx,data in enumerate(li): #순서와 값을 같이 알고 싶을때 
    print(idx,' ',data)
    
print('continue, break----')
datas = [1,2,3,4,5]
for i in datas:
     if i==2:break
     print(i,end='')
else:
    print('정상처리')


print()
li1 =[3,4,5]
li2 =[0.5,1,2]
for a in li1:
    for b in li2:
        print(a+b, end=' ')
        
print()
results= [a+b for a in li1 for b in li2]
for d in results:
    print(d,end=' ')
    
print('정규표현식, for 사용 연습: 다량의 문자열을 분리해 건수 출력')
import re
ss= '''
김정은 조선노동당 총비서 겸 국무위원장은 “10월 초부터 북남 통신연락선들을 다시 복원하도록 
할 의사를 표명하셨다”고 30일 <노동신문>이 1면에 보도했다. 김정은 위원장은 “29일 최고인민회의 
14기5차 회의 2일 회의에서 역사적인 시정연설 '사회주의 건설의 새로운 발전을 
'''
#print(ss)
ss2= re.sub(r'[^가-힝\s]','',ss)
print(ss2)
ss3=ss2.split(' ')
print(ss3)
cou ={} # 단어 횟수를 dict로 저장

for i in ss3:
    if i in cou:
        cou[i]+=1 # 같은 단어가 있으면 누적
    else:
        cou[i]=1
print(cou)

print('dict type(사전형)의 변수로 과일값 계산')
price ={'사과':2000,'감':500, '배':3000} #개 당 가격
gogek_tom={'사과':2,'배':3}# 손님이 구매한 과일 갯수
bill= sum(price[f]*gogek_tom[f] for f in gogek_tom)
print('과일 값 총액: {}원'.format(bill))

print('\nfor문 한 줄로 코딩하기')
a=1,2,3,4,5,6,7,8,9,10
li =[]
for i in a:
    if i%2==0:
        li.append(i)
print(li)
#위 코드를 한 줄로 표현
print(list(i for i in a if i%2==0))

print()
datas = [1,2,'a',True,3.5]
li = [i*i for i in datas if type(i)==int]
print(li)

print()
datas ={1,1,2,2,3}
li2 = [i*i for i in datas]
print(li2)

print()
id_name ={1:'tom',2:'james'}
name_id ={val:key for key, val in id_name.items()}
print(name_id)

print()
aa =[(1,2), (3,4), (5,6)]
for a,b in aa:
    print(a+b)