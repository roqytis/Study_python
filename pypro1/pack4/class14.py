# 카페 24p 4번

from abc import *


class Employee(metaclass=ABCMeta):
    def __init__(self,irum, nai):
        self.irum= irum
        self.nai= nai
    
    @abstractmethod 
    def pay(self):
        pass
    @abstractmethod
    def data_print(self):
        pass

    def irumnai_print(self):
        print('이름은', self.irum,'나이',self.nai)

class Temporary(Employee):
    def __init__(self,irum, nai,ilsu,ildang):
        Employee.__init__(self, irum, nai)
        self.ilsu = ilsu
        self.ildang= ildang 
           
    
    def data_print(self):
        pass
    
    def pay(self):
        print('월급은', self.ilsu*self.ildang)
        
class Regular(Employee):
    def __init__(self, irum,nai,salary):
        Employee.__init__(self, irum, nai)
        self.salary=salary
    
   
    def pay(self):
        pass
    
    def data_print(self):
        print('이름: ',self.irum," 나이: ",self.nai,' 급여',self.salary)
   
class Salesman(Regular):
    def __init__(self, irum,nai,salary,sales,commission):
        Regular.__init__(self, irum, nai, salary)
        self.sales=sales
        self.commission=commission
    
    def pay(self):
        pass
    
    def data_print(self):
        pass
    
    def regular_print(self):
        print('이름: ',self.irum," 나이: ",self.nai,'수령액', self.salary+(self.sales*self.commission))
     
t=Temporary('홍길동',25,20,15000)
t.irumnai_print(),
t.pay()
r=Regular('한국인',27, 3500000)
r.data_print()
s=Salesman('손오공', 29, 1200000,5000000,0.25)
s.regular_print()