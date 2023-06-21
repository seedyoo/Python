'''
    시퀀스 내장 함수
    
    1. enumerate()
    
    2. range()
    
    3. len() 
    
    4. sorted()
    
    5. zip()

'''

# enumerate()
prog = ['Java', 'Python', 'C']
for item in enumerate(prog):
    print(item)             # (0, Java) ...
    
    
    
# range(10) : 0 1 2 3 4 5 6 7 8 9
for i in range(10):
    print(i, end=' ')
print()    


# range(1, 11) : 1 2 3 4 5 6 7 8 9 10
for i in range(1,11):
    print(i, end=' ')
print()    
    
    
# range(2, 21, 2) : 2 4 6 8 10 12 14 16 18 20
for i in range(2,21,2):
    print(i, end=' ')
print()    


# len
li = ['월','화','수','목','금','토','일']    
print(li)
print('li 요소의 개수 : {}'.format( len(li) ))


# sorted
# sorted( 리스트, reverse=False ) : 오름차순
# sorted( 리스트, reverse=True )  : 내림차순
scores = [100, 90, 65, 80, 70]
print(scores)
print( sorted(scores) )
print( sorted(scores, reverse=True) )
print( sorted(scores, reverse=False) )


# zip
names = ['s1','s2','s3','s4','s5']

for student in zip(names, scores):
    print(student)
    
    