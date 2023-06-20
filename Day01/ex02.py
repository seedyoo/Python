s = "안녕하세요"

# 문자열 선택 연산자        : [index]
# 인덱싱
# index 는 0 부터 시작하는 순서 번호
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 문자열 범위 선택 연산자   : [:]
# 슬라이싱
# [시작index : 끝index+1]
# index : 0~1
print( s[0:2] )         # 안녕

# 2~끝
print( s[2:] )          # 하세요

# 시작~2
print( s[:2] )          # 안녕

# IndexError
# 범위에 없는 인덱스를 접근할 때 예외 발생
# (예외) print( s[100] )

# 문자열 길이 : len()
print("문자열 길이 : " + str(len(s)) )      # str() : 문자열 자료형으로 변환