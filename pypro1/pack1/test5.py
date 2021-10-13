#tuple : list와 유사하나 읽지건용
#t =(1,2,3,4)
t=1,2,3,4,3
print(t, type(t),len(t))
print(t.count(3), t.index(4))

imsi=list(t)
print(imsi,type(imsi))
imsi[0]=10
t=tuple(imsi)#형변환
print(t,type(t))
aa=(1)
print(aa, type(aa))# 이건 int
bb=(1,)
print(bb, type(bb)) #이건 튜플

print('-----'*10)
# set : 순서 x,  중복x
a={1,2,3,1}
print(a, type(a), len(a))
#print(a[0]) #TypeError: 'set' object is not subscriptable

b={3,4}
print(b)
#print(a+b)#TypeError: unsupported operand type(s) for +: 'set' and 'set'
print(a.union(b))
print(a.intersection(b))
print(a|b, a-b,a&b)

a.update({6,7})
print(a)
a.remove(6)
print(a)

li = [1,2,2,3,2,1]
print(li)
s=set(li)
li=list(s)
print(li)

print('----'*10)
#dict : 순서x 키:값의 쌍으로 구성
mydic = dict(k1=1, k2='mbc', k3=3.4)
print(mydic,type(mydic))

dic={'파이썬':'뱀','자바':'커피','spring':'용수철', 'kbs':9}
print(dic, type(dic), len(dic))
print(dic['자바'])
#print(dic['커피']) #KeyError: '커피'

dic['오라클']='예언자'
print(dic)
del dic['오라클']
print(dic)
dic.pop('자바')
print(dic)
dic['spring']='웹용프레임워크'
print(dic)

print(dic.keys())
print(dic.values())
print(dic.get('파이썬'))
print(dic['파이썬'])
print('spring' in dic)
print('dfdring' in dic)
