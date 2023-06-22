
def secure_name(name):
    cnt = len(name) - 1
    return name[0] + ('*' * cnt)


def secure_no(no):
    return no[0:8] + '******'

def secure_phone(phone):
    return phone.replace( phone[4:8], '****' )
    

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