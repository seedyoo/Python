'''
    파일 입출력
    
    - 텍스트 파일에 추가하기
'''

# 파일 저장 경로
path = 'C:/YYS/Python/human_Python/Day03/'

# 파일 열기
# at : 추가모드, 텍스트모드
file = open(path + 'hello.txt', 'at', encoding='UTF-8')

# 추가할 내용
file.write('\n')
file.write('이어서 추가된 내용입니다.')
file.write('\n')
file.writelines('텍스트 파일 내용 추가 모드 : at \n')

# writelines() 
# :컬렉션의 여러 요소들을 가져와서 여러 줄의 문자열로 출력하는 함수
text_list = ['1번 줄\n', '2번 줄\n', '3번 줄\n',]
file.writelines(text_list)

print('파일에 새로운 내용을 추가하였습니다')

# 파일 닫기
file.close()


