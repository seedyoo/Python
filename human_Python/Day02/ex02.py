# 다중 조건문
# - 첫 번째 조건, (if)
#   첫 번째 조건이 만족하지 않았을 때, (elif)
#   두 번째 이상의 조건들이 모두 만족하지 않으면 else 문 실행

score = input('성적 : ')
score = int(score)


if score >= 90:
    print('A 학점 입니다.')
elif score >= 80:
    print('B 학점 입니다.')
elif score >= 70:
    print('C 학점 입니다.')
elif score >= 60:
    print('D 학점 입니다.')
else:
    print('F 학점 입니다.')
