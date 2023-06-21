'''
    숫자 내장 함수
    
1. abs()        : 절댓값
2. divmod()     : 몫과 나머지를 한 쌍으로 반환
3. float()      : 실수로 반환
4. int()        : 정수로 반환
5. max()        : 최댓값을 반환
6. min()        : 최솟값을 반환
7. pow()        : 거듭제곱을 반환
8. round()      : 인수1개 - 정수로 반올림
                  인수2개 - 2번째 인수만큼 소수점 자리를 표시
9. sum()        : 리스트나 튜플 등의 합계를 반환
'''

print('#1')
print( abs(-10) )

print('#2')
money = 10000
price = 3000
result = divmod(money, price)
print(type(result))
print('커피를 {}개 사고 {}원이 남았습니다'.format(result[0], result[1]))


print('#3')
a = '3.14'
print( float(a) + 0.06 )


print('#4')
b = '15'
print( int(b) + 5 )

print('#5')
# split()           : 입력받은 값을 공백을 기준으로 분리
x, y, z = input("정수 3개를 입력 : ").split()
x = int(x)
y = int(y)
z = int(z)
print('최댓값 : {}'.format( max(x,y,z) ))

print('#6')
print('최솟값 : {}'.format( min(x,y,z) ))


print('#7')
print('2^2 : {}'.format( pow(2,2)) )
print('3^2 : {}'.format( pow(3,2)) )


print('#8')
print('round(1.5) : {}'.format( round(1.5) ))
print('round(2.675,2) : {}'.format( round(2.675,2) ))


print('#9')
li = [1,2,3,4,5]
print('sum(li) = {}'.format( sum(li) ))

t = (10,20,30,40,50)
print('sum(t) = {}'.format( sum(t) ))