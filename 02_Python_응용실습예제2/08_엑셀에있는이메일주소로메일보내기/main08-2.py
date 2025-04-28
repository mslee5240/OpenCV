# 1. 필요한 패키지 가져오기
import openpyxl
import smtplib     # 파이썬을 사용하여 메일을 보낼수 있는 패키지
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# 2. 이메일 설정
'''
1. 네이버 메일에서 내 메일함의 설정 > [POP3/IMAP설정]탭 : IMAP/SMTP - 사용함으로 설정해줘야함
2. 구글 메일에서 모든 설정 보기 > [전달 및 POP/IMAP] 탭 : IMAP 사용 - 사용 선택
'''
your_email_address = "your_email"  # your_email : 본인의 이메일 주소를 입력하세요
your_email_password = "your_email_password"  # your_email_password : 본인의 이메일 비밀번호를 입력하세요.
smtp_server = "smtp.naver.com"  # SMTP 서버 주소
smtp_port = 465  # SMTP 서버 포트 번호 , TLS 경우 port 587

# 3. 엑셀 파일 열기
wb = openpyxl.load_workbook('08_엑셀에있는이메일주소로메일보내기\email_list.xlsx')
sheet = wb.active

# 4. 각 행의 이메일과 이름에 대해 메일 보내기
for row in sheet.iter_rows(min_row=2, values_only=True):  # 첫 번째 행은 제외
    email, name = row

    # 이메일 내용 작성
    subject = f"{name}님 환영합니다."
    body = f"{name}님 늦지 않게 와주세요."
    message = MIMEMultipart()
    message['From'] = your_email_address
    message['To'] = email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # 이메일 보내기
    #with smtplib.SMTP(smtp_server, smtp_port) as smtp:        # TLS 방식
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:    # SSL 방식
        #smtp.ehlo()
        #smtp.starttls()
        smtp.login(your_email_address, your_email_password)
        smtp.sendmail(your_email_address, email, message.as_string())

# 5. 엑셀 파일 닫기
wb.close()
