import qrcode
import os

# QR 코드에 넣을 데이터
data = "Hello, World!"

# QR 코드 생성 : qrcode 의 make() 사용하기
img = # code here

# 이미지 파일로 저장
file_path = os.path.join("04_QR코드생성기", "qrcode.png")
img.save(file_path)



