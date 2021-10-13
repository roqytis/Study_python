#내장된 모듈 읽기
#py는 모듈단위로 저장, 읽기,실행을 함
#멤버 : 변수, 명령문, 함수 , 클래스 다른 모듈 



print('무언가를 하다가... 외부모듈 읽기')

import sys
print('경로: ',sys.path)
#sys.exit(0) #프로그램의 강제 종료

import math
print(math.pi)
print(math.sin(math.radians(30)))

import calendar
calendar.setfirstweekday(6)
calendar.prmonth(2021,10)

print()
import os
print(os.getcwd())
print(os.listdir('./'))

print('난수 출력')
import random
print(random.random())
print(random.randrange(1, 10))

print()
from random import random, randrange
print(random())
print(randrange(1, 10))

from random import *

print('프로그램 종료')