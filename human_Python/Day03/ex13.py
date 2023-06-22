'''
    CSV (Comma Separated Value)
    : 콤마(,) 분리한 값들
    
    
    ex) 
        학번,이름,주소,전화번호
        101,김휴먼,서울시 영등포구,010-1111-2222
        102,김휴먼,서울시 영등포구,010-1111-2222
        103,김휴먼,서울시 영등포구,010-1111-2222
        104,김휴먼,서울시 영등포구,010-1111-2222
        
'''
import csv

path = 'C:/YYS/Python/human_Python/Day03/'
file = input('파일명 : ')
file = path + file      

with open( file, 'w', newline='', encoding='UTF-8' ) as file:
    # csv 파일 객체
    csv_maker = csv.writer(file, delimiter=',')
    
    csv_maker.writerow(['학번','이름','주소','전화번호'])
    csv_maker.writerow(['101','김휴먼','서울시 영등포구','010-1111-2222'])
    csv_maker.writerow(['102','김휴먼','서울시 영등포구','010-1111-2222'])
    csv_maker.writerow(['103','김휴먼','서울시 영등포구','010-1111-2222'])
    csv_maker.writerow(['104','김휴먼','서울시 영등포구','010-1111-2222'])
    
    
print('파일이 생성되었습니다')
    
    
    