#키보드로 동이름을 입력해 해당 자료 읽기
try:
    dong =input('동이름 입력: ')
    
    with open('zipcode.txt', mode='r', encoding='euc-kr') as f:
       line = f.readline()
       #print(line)
       while line:
          # lines = line.split('\t')
           lines = line.split(chr(9)) #10진수 9를 아스키 코드로 탭키
           #print(lines)
           
           if lines[3].startswith(dong):
               #print(lines)
               print('['+lines[0]+']'+' '+lines[1] +\
                     ' '+lines[2] + ' '+lines[3]+' ' +lines[4])
               
           line =f.readline()
    
        
except Exception as e:
    print(('err: ', e))