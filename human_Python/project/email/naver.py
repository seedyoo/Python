'''
    파이썬으로 이메일 전송하기
    
    * 준비하기
    - 라이브러리 설치
    - 이메일 로그인해서 IMAP, POP3 설정하기
    
    1. 라이브러리 설치
    * smtplib   : 이메일 전송하기 위한 모듈
    * email     : 이메일 메시지, 첨부파일 등 관리를 위한 모듈
    - 기본 라이브러리라서, 별도 설치 필요X
    
    2. 이메일 SMTP 설정하기
    - (네이버 메일)
        > 환경 설정 > IMAP/POP3 설정
        > SMTP/POP3 사용함 ✅
        > 네이버 메일이 원본 저장 ✅
    
    3. 네이버 로그인 2단계 인증 > 해제
    
    4. stmp_port : 587
'''
import smtplib
from email.mime.text import MIMEText    # 이메일 텍스트 형식 모듈


print('네이버 이메일 보내기')

# 서버 정보, 로그인 정보
smtp_info = {
            'smtp_server'   : "smtp.naver.com",           # SMTP 서버 주소
            'smtp_user_id'  : input("네이버 메일주소 : "),
            'smtp_user_pw'  : input("비밀번호 : "),
            'smtp_port'     : 587,                        # SMTP 서버 포트
            }

# 이메일 전송 
def send_email(smtp_info, msg):
    mail_server = smtp_info["smtp_server"]
    port = smtp_info["smtp_port"]
    with smtplib.SMTP(mail_server, port) as server:
        # TLS 보안 연결
        server.starttls()
        
        # 로그인
        id = smtp_info["smtp_user_id"]
        pw = smtp_info["smtp_user_pw"]
        server.login(id, pw)
        
        # 이메일 전송
        # sendmail(보내는사람, 받는사람, 메시지 문자열)
        sender = msg['From']
        receiver = msg['To']
        response = server.sendmail( sender, receiver, msg.as_string() )
        
        # 전송결과 확인
        if not response:
            print('이메일을 성공적으로 보냈습니다')
        else:
            print('응답결과 : ')
            print(response)

# send_email 함수 끝


# 이메일 내용 입력
receiver = input('받는 사람 : ')        # 받는 사람
sender = smtp_info['smtp_user_id']      # 보내는 사람
title = input('제목 : ')
content = input('내용 : ')


# 메일 객체 생성
msg = MIMEText(_text = content, _charset = "utf-8")
msg['Subject'] = title
msg['From'] = sender
msg['To'] = receiver


# 이메일 전송
send_email(smtp_info, msg)


