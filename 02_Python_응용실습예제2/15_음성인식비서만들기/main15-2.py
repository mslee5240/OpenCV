# 0. 패키지 설치하기 
# [terminal ] pip install SpeechRecognition

# 1. 패키지 가져오기
import speech_recognition as sr
import webbrowser

# 2. 음성인식을 위한 객체 생성
r = sr.Recognizer()

# 3. 음성 입력 받기
with sr.Microphone() as source:
    print("말씀하세요...")
    audio = r.listen(source)

# 4. 음성 인식
try:
    text = r.recognize_google(audio, language='ko-KR')
    print(f"인식된 음성: {text}")
    
    # 음성 명령에 따라 동작 수행
    if "구글" in text:
        webbrowser.open("https://www.google.com")
    elif "유튜브" in text:
        webbrowser.open("https://www.youtube.com")
    elif "검색" in text:
        query = text.split("검색")[1]
        webbrowser.open(f"https://www.google.com/search?q={query}")
    else:
        print("해당 명령을 이해할 수 없습니다.")
except sr.UnknownValueError:
    print("음성 인식에 실패했습니다.")
