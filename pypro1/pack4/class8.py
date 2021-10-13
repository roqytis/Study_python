#상속

class Person:
    say = '난 사람이야~~~'
    nai = 20
    __abc = 'good' #private 멤버변수 (현재 클래스에서만 유효)
    
    def __init__(self,nai):
        print('Person 생성자')
        self.nai=nai
        
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai,self.say))
        
    def hello(self):
        print('안녕')
        print(self.__abc) 
           
print(Person.say, Person.nai)
# Person.printINfo()  x
p = Person('22')
print(p.say,p.nai)
p.printInfo()
p.hello()
#print(p.__abc) #AttributeError: 'Person' object has no attribute '__abc'

print('***'*10)
class Employee(Person):
    say = '일하는 동물'
    subject ='근로자'
   
    def __init__(self):
        print('Employee 생성자!')
     
       
    def printInfo(self):
        print('Employee 클래스에서 오버라이드한 pritInfo')
     
    
    def e_printInfo(self):
        self.printInfo()
        super().printInfo() #이건 처음부터 부모메소드를 호출
        print(self.say, super().say)
        self.hello()
        #print(self.__abc) #AttributeError: 'Employee' object has no attribute '_Employee__abc'

        
e = Employee()
print(e.say, e.nai, e.subject)
e.printInfo()
e.e_printInfo()

print('~~~~'*10)
class Worker(Person):
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai) #부모 클래스의 생서자 호출, bound method call
    
    def w_printInfo(self):
        self.printInfo()

w = Worker('25')
print(w.say, w.nai)
w.w_printInfo()

print('^^^'*10)
class Programmer(Worker):
    def __init__(self,nai):
        print('Programmer 생성자')
        #super().__init__(nai) #아래와 같은 거임
        Worker.__init__(self, nai) #부모클라스 생서자 호출. unbound method call
    
    def p_printInfo(self):
        self.printInfo()

pr = Programmer('33')
print(pr.say, pr.nai)
pr.p_printInfo()

print('---클래스 타입 확인------')
a = 10; print(type(a))
print(type(pr))
print(type(w))
print(Programmer.__bases__)
print(Worker.__bases__)
print(Person.__bases__)