#다른 모듈에서 호출될 사용자 정의 모듈
tot=100

def listTotal(*ar):
    print(ar)
    print(__name__)
    if __name__ == '__main__': #현재 모듈이 메인이면 참
            print('리스트 토탈 함수 실핼')
    
def kbs():
    print('대한민국 공영방송')

def mbc():
    print('mbc 넘버원 채널')