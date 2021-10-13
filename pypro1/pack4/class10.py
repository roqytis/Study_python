#다중 상속
class Tiger:
    data ='호랑이 세상'
    
    def cry(self):
        print('호랑이 : 어흥')
        
    def eat(self):
        print('맹수는 고기를 좋아함')

class Lion:
    def cry(self):
        print('사자 : 으르렁')
        
    def hobby(self):
        print('백수의 왕은 낮잠이 취미~')
        
class Liger1(Tiger, Lion): #다중 상속 순서가 중요하다 tiger먼저씀
    pass

lig1 = Liger1()
lig1.cry()
lig1.eat()
lig1.hobby()
print(lig1.data)

print('************************')
class Liger2(Lion, Tiger):
    data= '라이거 만세'
    
    def play(self):
        print('라이거 고유 메소드')
        
    def hobby(self):
        print('라이거의 취미는 프로그래밍')
        
    def showHobby(self):
        self.hobby()
        super().hobby()
        print(self.data,' ',super().data)
        
lig2 =Liger2()
lig2.cry()
lig2.showHobby()