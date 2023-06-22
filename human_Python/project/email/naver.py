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
        > 환경 설정 > IMAP/POPR 설정
        > SMTP/POP3 사용함 ✅
        > 네이버 메일이 원본 저장 ✅
    
    3. 네이버 로그인 2단계 인증 > 해제
    
    4. stmp_port : 587
'''
import smtplib
from email.mime.text import MIMEText    # 이메일 텍스트 형식 모듈
