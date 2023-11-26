import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

# 사용자에게 이메일 정보 입력 받기
sender_email = input("Enter your email address: ")
sender_password = getpass.getpass("Enter your email password: ")
receiver_email = input("Enter the recipient's email address: ")

# 이메일 서버 설정 (Gmail의 경우)
smtp_server = "smtp.gmail.com"
smtp_port = 587

# 이메일 내용 입력 받기
subject = input("Enter the subject of the email: ")
body = input("Enter the body of the email: ")

# MIMEText를 사용하여 이메일 내용 설정
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# SMTP 서버에 연결 및 로그인
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(sender_email, sender_password)

    # 이메일 보내기
    server.sendmail(sender_email, receiver_email, message.as_string())

print("이메일이 성공적으로 전송되었습니다.")