import datetime

# [모듈].[객체].메소드()
nowtime = datetime.datetime.now()
print('현재 날짜와 시간 : {}'.format(nowtime))

today = datetime.date(2023, 6, 22)
print('오늘 날짜 : {}'.format(today))


lastDay = datetime.date(2023,10,31)
print('종강일 : {}'.format(lastDay))


t1 = datetime.time(11, 20, 0)
print('현재 시간 : {}'.format(t1))

t2 = datetime.time(17, 40, 0)
print('수업 종료 : {}'.format(t2))


print( datetime.datetime.today().strftime('%Y-%m-%d') )

today = datetime.datetime.now()
print('{} 년'.format( today.year) )
print('{} 월'.format( today.month) )
print('%02d 월' % today.month )         # leading zero (01~09)
print('{} 일'.format( today.day) )
print('{} 시'.format( today.hour) )
print('{} 분'.format( today.minute) )
print('{} 초'.format( today.second) )





