import cx_Oracle

# 데이터베이스 연결 정보
dsn = cx_Oracle.makedsn(host='localhost', port='1521', sid='orcl')
username = 'human'
password = '123456'

# 데이터베이스 연결
connection = cx_Oracle.connect(username, password, dsn)