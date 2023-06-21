# for 문

# 리스트 반복
li = [1,2,3,4,5]

for item in li:
    print(item, end=' ')
    
print()
    
# range() 함수 사용한 반복
for item in range(1,6):
    print(item, end=' ')
    
print()
    
# 1~20 까지의 홀수를 출력하시오
for item in range(1,20,2):
    print(item, end=' ')


print()

# 문자열 반복
s = "안녕하세요"
for item in s:
    print(item, end=' ')