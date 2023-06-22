import time

# time() : 1970년 1월 1일 0시 0분 0초 부터 경과한 시간을 반환
print('time : {}'.format( time.time() )) 

# ctime(시간) : 날짜/시간 형식으로 변환하는 함수
t = time.time()
print('ctime() : {}'.format( time.ctime(t) ))


'''
    날짜 형식 지시자
    %y      :   2자리 년도 (23)
    %Y      :   4자리 년도 (2023)
    %m      :   2자리 월(01~12)
    %b      :   3자리 영문 월(Jan~Dec)
    %B      :   전체 영문 월(January~December)
    %d      :   2자리 일(01~31)
    %a      :   3자리 요일(Sun~Sat)
    %A      :   전체 영문 요일(Sunday~Saturday)
    %I      :   12시 시간(01~12)
    %H      :   24시 시간(00~23)
    %M      :   분(00~59)
    %S      :   초(00~59)
'''

# 2023/06/22 (Thu) 11:20:00
s = time.strftime('%Y/%m/%d (%a) %H:%M:%S')
print('strftime() : {}'.format(s))


# 지정한 시간(초)만큼 시스템을 일시중지
time.sleep(5)               # 5초간 중지

print('5초 후...')