#thread 간 공유자원 값 충돌 방지

import threading
import time

g_count = 0 #전역변수는 스레드의 공유자원 대상
lock = threading.Lock()

def threadCount(id, count):
    global g_count
    for i in range(count):
        lock.acquire() #락을 거어 특정 스레드가 공유자원을 사용하는 동안 다른 스레드를 작업대기
        print('id %s ==> count: %s, g_count: %s' %(id,i,g_count))
        g_count=g_count + 1
        lock.release()#lock 해제
        
for i in range(1,6):
    threading.Thread(target=threadCount, args=(i, 5)).start()      
    
time.sleep(1)
print('최종 g_count:', g_count)
print('finish')