# format() 메소드
# {} 괄호 기호를 변수나 값이 표시될 위치(형식)을 
# 지정하여 출력하는 메소드

print('내 이름은 {}'.format('김휴먼'))


a = 10
b = 20
print('a : {}, b : {}'.format(a, b))

# index 를 지정하여 사용할 수도 있다
print('b : {1}, a : {0}'.format(a, b))


a = '안녕'
b = '김휴먼'
print('{0}하세요~! 저는 {1} 입니다. 집에 갑시다. {0} - {1} 올림 - '.format(a,b))


tel1, tel2, tel3 = '02', '3667', '3688'
print('연락처 : {0}-{1}-{2}'.format(tel1, tel2, tel3))


academy = 'HUMAN'
print('name : {name}'.format(name=academy))