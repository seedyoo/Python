# 리스트
# : 서로 다른 자료형의 값을 저장할 수 있는 컬렉션

# li = [값, 값2, ...]
li = [100, 12.34, 'hello']
print('li : ', li)


# 리스트 인덱싱
print('li[0] : ', li[0])
print('li[1] : ', li[1])
print('li[2] : ', li[2])


# 리스트의 슬라이싱
li2 = ['월','화','수','목','금','토','일']
print('li2[0:5] : ',li2[0:5])
print('li2[:5] : ',li2[:5])

print('li2[5:7] : ',li2[5:7])
print('li2[5:] : ',li2[5:])


# 요소 추가 및 삭제
# - 요소 추가 : append(), insert()
# - 요소 삭제 : pop()

li3 = [1,2,3,4,5]
# append(요소)              : 마지막에 요소 추가
print('### append() ###')
li3.append(6)
print(li3)

li3.append(7)
print(li3)

# insert(인덱스,요소)       : 인덱스에 요소 추가
print('### insert() ###')
li3.insert(2, 2.5)
print(li3)

# pop(인덱스)               : 인덱스의 요소 삭제
# pop()                     : 마지막 요소 삭제
print('### pop() ###')
li3.pop(2)
print(li3)

li3.pop()
li3.pop()
print(li3)