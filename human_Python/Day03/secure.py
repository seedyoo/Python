# 모듈 : secure

def secure_name(name):
    cnt = len(name) - 1
    return name[0] + ('*' * cnt)

def secure_no(no):
    return no[0:8] + '******'

def secure_phone(phone):
    return phone.replace( phone[4:8], '****' )