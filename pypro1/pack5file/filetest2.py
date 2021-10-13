#with 구문을 사용하면 close() 자동 지원

try:
    # 파일 저장
    with open('ftest3.txt', mode='w', encoding='utf-8') as f1:
        f1.write('요즘 날씨가 계속 흐려\n')
        f1.write('몸이 찌푸둥\n')
        f1.write('close 자동으로 해줌\n')
    print('저장 완료')
    
    #파일 일기
    with open('ftest3.txt', 'r', encoding='utf-8') as f2:
        print(f2.read())
except Exception as e:
    print('err :', e)
    
print('\n피클링(객체를 저장하고 읽기)--')
import pickle

try:
    dictData = {'tom':'111-1111', '현승':'222-2222'}
    listData=['박소영', '박정수']
    tupleData=(dictData,listData)
    
    with open('hello.dat','wb') as f3:
        pickle.dump(tupleData, f3) #객체를 저장
        pickle.dump(listData, f3) #객체를 저장
    print('객체를 파일로 저장 완료')
    
    with open('hello.dat','rb') as f4:
        a, b =pickle.load(f4)
        print(a)
        print(b)
        c = pickle.load(f4)
        print(c)
except Exception as e:
    print('err2 :', e)