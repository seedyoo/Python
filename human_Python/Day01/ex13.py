# 표준 출력 사용법
# 기본 출력
print('재미있는 파이썬')

# 콤마(,) 사용하기
num = 10
print('변수 num :',num)

# 분리된 데이터에 구분자 넣기
print('Python','C','Java')              # 바로 연결
print('Python','C','Java', sep=',')     # , 로 구분

# 한 줄에 출력하기
print('이름 ', end=': ')
print('김휴먼')

# 파일에 출력하기
# mode : wt
# - w : 쓰기모드 (write)
# - t : 텍스트 파일 (text)
fos = open('sample.py', mode='wt')
print('print("Hello Python~!")', file=fos)