#파이썬 모듈의 값을 html로 출력
my ='파이썬 변수 값'
tot= 70+80

print('Content-type:text/html;charset=utf-8\n')
print('<html><body>')
print('<b>안녕하세요</b> 파이썬 모듈로 작성한 문서입니다.<br>')
print('와우 성공')
print('<br>변수값 : %s, 하나더: %d'%(my,tot))
print('</body></html>')