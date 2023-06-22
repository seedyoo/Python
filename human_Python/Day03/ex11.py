# 파일 삭제
# os 모듈에 파일 삭제 기능이 정의되어 있다

import os

# 파일 저장 경로
path = 'C:/YYS/Python/human_Python/Day03/'
file = input('삭제할 파일명 : ')
file = path + file

# 파일 존재 확인
if os.path.exists(file):
    # 파일 삭제
    os.remove(file)
    print('파일이 삭제되었습니다')
    
    
