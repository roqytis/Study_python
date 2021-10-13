# 조건판단문 if


var = 2


if var>=3:
    print('크구나')
    print('참일 떄')
    #pass
else:
    print("거짓일떄")
print('end1')

print()
money=1000
age= 23
if money>=500:
    item='apple'
    if age<= 30:
        msg='young'
    else:
        msg='old'
else:
    item='pear'
    if age<= 20:
        msg='adult'
    else:
        msg='child'        
print(item,msg)
print('end2')

print()

jumsu=85
if jumsu>= 90:
    print('우수')
else:
    if jumsu>=70:
        print('보통')
    else:
        print("저조")
        
if jumsu>=90:
    print('우수2')
elif jumsu>= 70:
    print('보통2')
else:
    print("저조")
    
print('end3')

#jum = input('점수 입력:')
#print(jum,type(jum))
'''
jum = int(input('점수 입력:')) #키보드로 인풋하기 
#print(jum,type(jum))
if jum>= 90:
    print('good')
elif jum>= 70:
    print('nice')
else:
    print('normal8')
    
print()
if 90<= jum<=100:
    print('good2')
elif 70<= jum<90:
    print('nice2')
else:
    print('normal2')    
 '''   
print()
names =['홍길동','신선해','이겨라']
if '홍길동' in names:  #NOT IN
    print('맞아 내친구')
else:
    print('내친구 아닌데?')
    
print()
a ='kbs'
b =9 if a=='kbs' else 11
print(b)

a=11
b= 'mbc' if a==9 else'kbs'
print(b)

print()
a=3
if a<5:
    print(0)
elif a<10:
    print(1)
else:
    print(2)
    
#한줄로
print(0 if a<5 else 1 if a< 10 else 2)

print()
a=5
result= a*2 if a>3 else a+2
print('result: '+str(result))
                    
