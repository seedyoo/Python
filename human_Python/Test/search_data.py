from search import *

search_info = getSearchList()
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

def insertSearch(title,num):
    # SQL
    sql = '''INSERT INTO search (title, num)
             VALUES(%s, %s)
    
          '''
    # 데이터
    values = (title, num)
    
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


titles = search_info[0]
nums = search_info[1]
# rates = movie_info[2]
# dates = movie_info[3]

print('검색어 순위 개수 : ', len(titles))

for i in range(len(titles)):
    title = titles[i]
    num = nums[i]
    # rate = rates[i]
    # date = dates[i]
    #print(title, point, rate, date)
    insertSearch(title, num)


