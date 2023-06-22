'''
    파일 복사
    
    원본 파일 --> 변수 --> 복사본
    (읽기)                (쓰기)
    
    1. 원본 파일 읽기
    2. 1024Bytes(1KB) 씩 읽어온다
    3. 1024Bytes(1KB) 씩 저장한다
    4. 입력, 출력 close(종료)
    
    with
    : 파일 입출력 시, 자동으로 close() 함수를 호출한다
    
    with open(파일경로, 모드) as 파일 객체:
        처리 코드
        처리 코드
        처리 코드

'''
path = 'C:/YYS/Python/human_Python/Day03/'
file = input('가져올 파일명 : ')
copy = input('복사할 파일명 : ')
copy = path + copy      # 사본 경로
file = path + file      # 원본 경로

buffer_size = 1024          # 버퍼 용량 : 1024Byte(1KB)
# source        : 원본 파일 객체
# copyfile      : 복사 파일 객체
with open( file, 'rb' ) as source:
    with open( copy, 'wb' ) as copyfile:
        while True:
            # 원본 파일에서 1KB 씩 읽어옴
            buffer = source.read(buffer_size)
            if not buffer:
                break
            # 1KB 씩 파일 출력 (복사)
            copyfile.write(buffer)
            
            
print(copy)
print('파일이 복사되었습니다.')