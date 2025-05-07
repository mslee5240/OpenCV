# qrcode 모듈이 설치되어 있지 않다면 terminal 에서 설치하기 : pip install qrcode
import qrcode
import os

# QR 코드에 넣을 데이터
data = "Hello, World!"

# QR 코드 생성
img = qrcode.make(data)

# 이미지 파일로 저장
file_path = os.path.join("04_QR코드생성기", "qrcode.png")
img.save(file_path)



