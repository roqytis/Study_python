#백준 브론즈 3 2884번
#hour, min = map(int,input().split())
#hour, min = map(int,input().split())
hour =int(input('시간 입력: '))
min =int(input('분 입력: '))
if min >= 45:
    print(hour, min-45)
elif hour>0 and min < 45:
    print(hour-1, min+15)
else:
    print(23, min+15)