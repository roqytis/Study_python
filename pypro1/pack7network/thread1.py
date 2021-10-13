#thread: 스레드는 프로세스와 유사하나 같은 프로세스 내에서 수행되며 같은 실행환경을 공유한다는
#점에서 프로세스와 다르다. 스레드는 메인 프로세스(스레드)와 병렬적으로 수행되는 '미니 프로세스'라고 볼 수 있다. 
# 스레드를 이용하면 멀티 태스킹이 가능해 진다. 

import threading,time

def run(id):
    for i in range(1,10):
        print('id:{}--> {}'.format(id,i))
        time.sleep(0.5)
'''        
#스레드를 사용하지 않는 경우
run('일')
run('둘')
'''
# 스레드를 사용한 경우
th1=threading.Thread(target=run, args=('하나',))
th2=threading.Thread(target=run, args=('둘',))
th1.start()
th2.start()
print()
th1.join() #사용자 정의 스레드가 종료될 때까지 메인스래드 대기
th2.join()
print('프로그램 종료')