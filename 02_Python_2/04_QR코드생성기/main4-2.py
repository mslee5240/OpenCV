# 1. 필요한 패키지 가져오기
import qrcode
import os

# 2. 데이터가 저장된 파일 경로
file_path = os.path.join("04_QR코드생성기", "qrdata.txt")

# 3. QR 코드 생성 함수
def create_qrcode(data):

    # QR 코드 생성
    img = # code here
    
    # 이미지 파일로 저장
    img_file_path = os.path.join("04_QR코드생성기", f"qrcode_{data}.png")
    # code here

# 4. qrdata.txt 파일에서 데이터 읽어오기
with open(file_path, 'r') as f:
    for line in f:
        # 개행 문자 제거
        data = line.strip()
        # QR 코드 생성 함수 호출하기
        # code here 