# 조건문
# if
#   if 조건식 : 
#   (들여쓰기) 조건이 참일 때 실행할 문장

age = input("당신의 나이는?")
age = int(age)

if age >= 20:
    print('성인입니다')
    print('나이 : {} '.format(age))
else:
    print('청소년 입니다')
    print('나이 : {} '.format(age))