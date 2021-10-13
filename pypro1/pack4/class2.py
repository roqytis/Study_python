class Car: # 클래스의 이름은 대문자로 시작(권장)
    handle = 0  #멤버 변수 - prototype
    speed = 0
    
    def __init__(self,name,speed): #name, speed 지역변수
        self.speed=speed
        self.name=name
        
    def showData(self):
        km='킬로미터' #메소드내에서 유효한 지역변수
        msg='속도: '+str(self.speed)+ km+', 핸들 수 :'+str(self.handle)
        return msg
    
print(id(Car),Car.handle, Car.speed) # 참고로 원형 클래스 멤버 출력
print()
car1 =Car('tom',10) #생성자를 호출하며 car1을 포함해서 세개의 인수를 전달
print(car1.speed,car1.handle,car1.name)
car1.color='파랑'
print(car1.color)
print()
car2= Car('제임스',50)
print(car2.speed,car2.handle,car2.name)
print()
print('주소출력: ', id(Car), id(car1), id(car2))
print(Car, car1, car2) #Car, Car object, Car object
print()
print(Car.__dict__) #각 객체의 멤버를 확인하는 명령
print(car1.__dict__) #{'speed': 10, 'name': 'tom', 'color': '파랑'}
print(car2.__dict__)#{'speed': 50, 'name': '제임스'}

print('\n메서드 호출---')
print('car1 메소드 : ', car1.showData())
print('car2 메소드 : ', car2.showData())
car1.speed=100
car2.speed =120
print('car1 메소드 : ', car1.showData())
print('car2 메소드 : ', car2.showData())
print()
print(Car.speed)
print(car1.speed)
print(car2.speed)