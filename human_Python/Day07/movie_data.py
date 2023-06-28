from movie import *

movie_info = getMovieList()
# print(movie_info)

import pymysql

host = 'localhost'
port = 3306
user = 'root'   # human
password = '123456'  #123456
database = 'human'                 #스키마

# MySQL 연결
connection = pymysql.connect(
    host = host,
    port = port,
    user = user,
    password = password,
    database = database
)
# 
if connection:
    print('MySQL 연결되었습니다.')

# --------------------------------

# print( movie_info[0] )
# print( movie_info[1] )
# print( movie_info[2] )
# print( movie_info[3] )

def insertMovie(title, point, rate, date):
    # SQL
    sql = '''INSERT INTO movie (title, point, rate, date)
             VALUES(%s, %s, %s, %s)
    
          '''
    # 데이터
    values = (title, point, rate, date)
    
    try:        
        # 커서 생성
        with connection.cursor() as cursor:
            cursor.execute(sql, values)
        
        # 변경 사항 적용
        connection.commit()
        print('데이터 추가 완료...')
    
    except pymysql.Error as e:
        print("MySQL Error : ", e)
    
    # finally:
    #     connection.close()
    
    return


titles = movie_info[0]
points = movie_info[1]
rates = movie_info[2]
dates = movie_info[3]

print('영화정보 개수 : ', len(titles))

for i in range(len(titles)):
    title = titles[i]
    point = points[i]
    rate = rates[i]
    date = dates[i]
    #print(title, point, rate, date)
    insertMovie(title, point, rate, date)


