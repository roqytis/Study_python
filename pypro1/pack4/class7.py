# 클래스의 상속 : 자원의 재활용이 목적
class Animal:
    nai=1
    
    def __init__(self):
        print('Animal 생성자')
    
    def move(self):
        print('움직이는 생물')
        
class Dog(Animal): #클래스의 상속
    def __init__(self):
        print('Dog 생성자')
        
    def my(self):
        print('난 댕댕이라고 해요')
        
dog1=Dog()
dog1.my()
dog1.move()
print(dog1.nai)

print('---')
class Horse(Animal):
    pass

horse1 =Horse()
horse1.move()
print(horse1.nai)