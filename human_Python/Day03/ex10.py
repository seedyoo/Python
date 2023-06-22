'''
    파일 입출력
    - 텍스트 파일 읽기
'''

# 파일 저장 경로
path = 'C:/YYS/Python/human_Python/Day03/'

# 파일 열기
# rt : 읽기모드, 텍스트모드
file = open(path + 'hello.txt', 'rt', encoding='UTF-8')

while True:
    str = file.readline()       # 파일로부터 한 줄 씩 읽어온다
    # str = file.read(10)         # 파일로부터 10글자 씩 읽어온다
    if not str:                 # ''(빈문자열)에 not 연산 시, False -> True
        # print(str)
        break
    print( str, end='' ) 
    
    
# 파일 닫기 
file.close