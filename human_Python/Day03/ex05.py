# random
import random

# random() : 0.0xxx ~ 0.9xxx 임의의 실수
print('random.random() : {}'.format(random.random()) ) 

# randint(a, b)     : a 이상 b 이하의 임의의 정수
print('random.randint() : {}'.format(random.randint(1, 10)) ) 


# randrange(a, b, c)     : a 이상 b 이하의 c만큼 증가하는 임의의 정수
print('random.randrange() : {}'.format(random.randrange(1, 10, 2)) ) # 1 3 5 7 9


# choice(A) : 시퀀스 자료형에 속한 요소 중 임의의 요소를 반환하는 함수
seasons = ['봄', '여름', '가을', '겨울']
print('내가 좋아하는 계절은 {} 입니다'.format( random.choice(seasons)) )

# sample(A, N) : 시퀀스 자료형에 속한 요소 중 지정한 개수의 요소를 임의로 반환하는 함수
lotto = range(1, 46)    # 1~45
lotto = random.sample(lotto, 6)
lotto = sorted(lotto)
print('이번 주 당첨 번호는 {}'.format( lotto ))


# shuffle(A)    : 시퀀스 자료형에 속한 요소들의 순서를 임의로 섞는 함수
#               A의 요소들의 순서를 섞는다
li = [1,2,3,4,5,6]
random.shuffle(li)
print('random.shuffle(li) : {}'.format( li ))


