'''
    pip install pymysql
    pip install cryptography
'''

import pymysql

# MySQL 서버 연결 정보
host = 'localhost'      
port = 3306
user = 'human'
password = '123456'
database = 'human'          # 스키마

# MySQL 연결
connection = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

# 연결 성공 여부 확인
if connection:
    print('MySQL 연결되었습니다.')


# board 테이블 조회
def selectAll():
    try:
        # 커서 생성
        cursor = connection.cursor()
        
        # SELECT 
        sql = "SELECT * FROM board"
        cursor.execute(sql)
        
        # 결과 가져오기
        result = cursor.fetchall()
        
        # 결과 출력
        for row in result:
            print(row)
        
    except pymysql.Error as e:
        print("MySQL Error : ", e)
        
    finally:
        # 커서와 연결 종료
        cursor.close()
        connection.close()
        
        
# board 테이블에 추가
def insert():
    
    try:
        # 커서 생성
        cursor = connection.cursor()
        
        # INSERT
        title = input('제목 : ')
        writer = input('작성자 : ')
        content = input('내용 : ')
        sql = "INSERT INTO board(title, writer, content) VALUES(%s, %s, %s)"
        
        # %s 에 데이터 매핑
        values = (title, writer, content)
        cursor.execute(sql, values)
        
        # 변경 사항 적용
        connection.commit()
    except pymysql.Error as e:
        print("MySQL Error : ", e)
    
    finally:
        cursor.close()
        connection.close()
        
        
        
# board 테이블 수정
def update():
    try:
        # 커서 생성
        cursor = connection.cursor()
        
        # UPDATE
        board_no = input('글번호 : ')
        title = input('제목 : ')
        writer = input('작성자 : ')
        content = input('내용 : ')
        sql = '''
            UPDATE board
               SET title = %s
                  ,writer = %s
                  ,content = %s
            WHERE board_no = %s
        '''
        
        # %s 에 데이터 매핑
        values = (title, writer, content, board_no)
        cursor.execute(sql, values)
        
        # 변경 사항 적용
        connection.commit()
    except pymysql.Error as e:
        print("MySQL Error : ", e)
    
    finally:
        cursor.close()
        connection.close()
        
        
# board 테이블에서 데이터 삭제
def delete():
    try:
        # 커서 생성
        cursor = connection.cursor()
        
        # DELETE
        board_no = input('글번호 : ')
        sql = '''
            DELETE FROM board
            WHERE board_no = %s
        '''
        
        # %s 에 데이터 매핑
        values = (board_no)
        cursor.execute(sql, values)
        
        # 변경 사항 적용
        connection.commit()
    except pymysql.Error as e:
        print("MySQL Error : ", e)
    
    finally:
        cursor.close()
        connection.close()
     
# insert()
selectAll()
# update()
# delete()


    

    
    
    
    
    
    