# 클래스 기본 이해
kor = 100

def abc():
    print('이건 함수')
    
class My:
    kor = 90
    
    def abc(self):
        print('요것은 메소드랍니다.')
        
    def show(self):
       # kor = 80
        print(kor)
        print(self.kor)   
        print()
        self.abc()
        abc()

my = My()
my.show()

print('**'*20)
class Our:
    a = 1
    
print(Our.a)
our1 = Our()
print(our1.a)

our1.a=2
print(our1.a)

print()
our2 =Our()
print(our2.a)
our2.kbs = 9
print(our2.kbs)

print()
Our.a=11
print(our1.a)
print(our2.a)