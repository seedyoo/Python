# 세트 반복
print('세트')
s = {1,2,3,4,5}
for item in s:
    print(item)
    


# 딕셔너리 반복
print('딕셔너리')
d = {
    'coffee'    : '커피',
    'human'     : '인간',
    'star'      : '별'
}

# 딕셔너리는 반복요소로 key가 반복된다.
for word in d:
    print('{} 의 뜻 \t : {}'.format(word, d.get(word) ))
