# 1. 필요한 패키지 가져오기
import requests   # 웹 페이지 요청을 위한 라이브러리
from bs4 import BeautifulSoup  # 웹 페이지 파싱을 위한 라이브러리
import tkinter as tk  # GUI 프로그래밍을 위한 라이브러리

# 2. 주가를 조회하는 함수
def get_stock_price():
    code = code_entry.get()  # Entry 위젯에서 사용자가 입력한 종목 번호 가져오기
    url = f'https://finance.naver.com/item/main.nhn?code={code}' # 네이버 금융 주소에 종목 번호 추가

    res = requests.get(url)  # 해당 URL로 요청 보내기
    soup = BeautifulSoup(res.content, 'html.parser')   # 받아온 웹 페이지를 파싱하기
    price = soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)') # 주가 정보가 있는 HTML 요소 선택
    result_label.config(text=f"현재 {code} 주가는 {price.text}입니다.") # 결과 레이블에 주가 정보 출력


# 3. 주가 조회 GUI 생성 - 005930 삼성전자 검색해보기
root = tk.Tk()     # 주 창 생성
root.title("주식 가격 조회 프로그램")  # 주 창의 제목 설정

label = tk.Label(root, text="종목 번호를 입력하세요:") # 레이블 생성
label.pack()       # 레이블을 주 창에 추가

code_entry = tk.Entry(root)   # 사용자가 종목 번호를 입력할 수 있는 Entry 위젯 생성
code_entry.pack()  # Entry 위젯을 주 창에 추가

button = tk.Button(root, text="조회", command=get_stock_price)  # "조회" 버튼 생성, 버튼 클릭 시 get_stock_price 함수 실행
button.pack()      # 버튼을 주 창에 추가

result_label = tk.Label(root, text="")  # 주가 정보를 출력할 레이블 생성
result_label.pack()  # 레이블을 주 창에 추가

# 4. GUI 프로그램 실행
root.mainloop()
