#묶음형 자료형 :str-순서를 갖음 수정 불가 : 슬라이싱 가능
s='sequence'
print(s)
print(len(s), s.count('e'), s.find('e'),s.find('e',3),s.rfind('e'))
print(s.startswith('s'), s.startswith('a'))
print()
ss='mbc'
print(ss,id(ss))
ss='abc'
print(ss,id(ss))

print('슬라이싱------')
print(s[0], s[2:4],s[:3],s[3:])

print()
s2='kbs mbc'
print(s2)
s3=s2.split(sep=' ')
print(s3)
s4=' ,'.join(s3)
print(s4)