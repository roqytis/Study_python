# 예외처리: 파일, 네트워크, 키보드, DB연동,나누기.....등의 작업을  하다가에러가 발생한 경우 대처하기
#카페 파이썬 3번
def divide(a,b):
    return a/b

#c= divide(5, 2)
#c= divide(5, 0) #ZeroDivisionError: division by zero
#print(c)

#에러에 대한 대처 작업: try~except

try:
    kbs=9
    
    c= divide(5, 2)
    #c= divide(5, 0) #0으로 못나눠서 에러
    print(c)
    
    aa=[1,2]
    print(aa[0])
    #print(aa[5])  #배열이 0, 1까지 밖에 없어서 에러
    
    f=open('c:/work/abc/txt') #이런 파일은 없엇 에러 FileNotFoundError: [Errno 2] No such file or directory: 'c:/work/abc/txt'
    
except ZeroDivisionError:
    print('두 번쨰 숫자는 0을 주면 안된당') #이건 내가 적어준 에러에 뜨는 창
except IndexError as e:
    print('참조 범위 오류 : ', e) #이건 콘솔에 뜨는 에러]
except Exception as e:    #이거 걍 모든 에러가 발생할떄 고통으로 사용
    print('에러발생 :', e)
finally:
    print('에러와 상관없이 반드시 수행된다.')
    del kbs
    
print('다음 작업 계속')