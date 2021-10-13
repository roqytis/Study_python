#추상 클래스 : 추상 메소드를 가지고 있는 클래스. 추상 클래스를 상속받은 자식 클래스는 반드시 추상메소드를 오버라이드 해야 한다. 
#추상클라스는 메소드 오버라이딩을 강요하려고, 다형성을 위해 오버라이딩을 강요한다. 
from abc import *

class TestClass(metaclass = ABCMeta): #추상 클래스가 됨. TestClass 타입의 객체 생성 불가
    
    @abstractmethod
    def abcMethod(self): #추상 메소드
        pass
    
    def normalMethod(self):
        print('추상 클래스 내의 일반 메소드')
        
#parent = TestClass() #TypeError: Can't instantiate abstract class TestClass with abstract methods abcMethod

'''
class Child1(TestClass):
    pass

#c1 =Child1() #TypeError: Can't instantiate abstract class Child1 with abstract methods abcMethod
'''
class Child1(TestClass):
    name ='난 Child1 멤버 변수'
    
    def abcMethod(self): #메소드 오버라이드 강요당함
        print('추상메소드를 오버라이드 함. 추상의 마법에서 풀림')
        
c1 = Child1()
print(c1.name)
c1.abcMethod()
c1.normalMethod()

print('---------')
class Child2(TestClass):
    
    def abcMethod(self): #강요
        print('추상메소드를 CHild2에서도 오버라이드 함')
        print('추상 메소드의 위력을 감ㅅ하하고 있음')
        
    def normalMethod(self): #선택
        print('추상 클래스 내의 이랍ㄴ 메소드는 오버라이드 해도 되고 안해도 되고 니맘이야~')
        
c2 = Child2()
c2.abcMethod()
c2.normalMethod()

print('--다형성--')
mbc =c1
mbc.abcMethod()
print()
mbc= c2
mbc.abcMethod()