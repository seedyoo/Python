# break
# : 현재 속한 반복문을 벗어나는 키워드

# 무한반복
# : 무조건 계속 반복하는 반복문
#   반드시, 종료조건 넣어주어야한다.

while True:
    city = input('살기 좋은 도시? ')
    # 종료조건
    if city == '서울': 
        print('정답입니다.')
        break
    else:
        print('틀렸습니다')
        
