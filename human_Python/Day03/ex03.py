
from secure import *

# 사용자 정보 마스킹하기
name = '김휴먼'
no = '880101-1234567'
phone = '010-1234-1234'

print( name )
print( no )
print( phone )
print()

print( secure_name(name) )
print( secure_no(no) )
print( secure_phone(phone) )