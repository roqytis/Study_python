#추상 클래스
# 프렌드라는 대표 클라스 만들고 존과 크리스

from abc import *

class Friend(metaclass=ABCMeta):
    def __init__(self,name):
        self.name=name
       
    @abstractmethod 
    def hobby(self):  #추상 메소드
        pass
    
    def printName(self): #일반 메소드
        print('이름은', self.name)
        
class John(Friend):
    def __init__(self, name,addr):
        Friend.__init__(self, name)
        self.addr=addr
    
    
    def hobby(self):  #오버라이딩
        print(self.addr+ '거리를 걸어다님')    
        
    def printAddr(self):  #존의 고유 메서드    
        print('주소는 '+ self.addr)
        
class Chris(Friend):
    def __init__(self, name,addr):
        Friend.__init__(self, name)
        self.addr=addr
        
    def hobby(self):  #오버라이딩
        print(self.addr+ ' 동네를 뛰어다님')
        print(self.addr + '에 살고 있다.')
        
john =John('존', '역삼동')
john.printName()
john.printAddr()
john.hobby()
print()
chris =Chris('크리스','사직동')
chris.printName()
chris.hobby()

print('-------------')
f = john
f.hobby()
f.printName
print()
f=chris
f.hobby()
f.printName()