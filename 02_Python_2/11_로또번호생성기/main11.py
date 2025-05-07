# 1. 패키지 가져오기
import tkinter as tk    #  GUI 프로그램 만들 때 사용하는 대표적인 라이브러리
import random

def generate_lotto_numbers():
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()
    return numbers

def generate_and_display_numbers():
    numbers = generate_lotto_numbers()
    number_label.config(text=" ".join(str(num) for num in numbers))

# 2. tkinter 윈도우 생성
window = tk.Tk()
window.title("로또 번호 생성기")
window.geometry("300x100")

# 3. 버튼과 번호 출력 레이블 생성
button = tk.Button(text="번호 생성", command=generate_and_display_numbers)
number_label = tk.Label(text="")
number_label.pack()

# 4. 버튼과 번호 출력 레이블 배치
button.pack(pady=10)
number_label.pack()

window.mainloop()
