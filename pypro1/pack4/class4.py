# 클래스로 새로운 타입 선언하기 : 가수 클래스(설계도)--> 객체 생성
print('뭔가를 하다가...')

class Singer: 
    title_song='화이팅 코리아'
    
    def sing(self):
        msg= '노래는'
        print(msg, self.title_song, '랄랄라~~')
        
bts = Singer()
print(type(bts))

bts.sing()
bts.title_song='버터'
bts.sing()
bts.co ='빅히트 엔터테이먼트'
print('소속사: ',bts.co)

print()
blackpink = Singer()
print(type(blackpink))
blackpink.sing()
#print('소속사 :',blackpink.co) 'Singer' object has no attribute 'co'

print(id(bts))
print(id(blackpink))
