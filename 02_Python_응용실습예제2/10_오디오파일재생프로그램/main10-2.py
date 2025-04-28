# 1. 패키지 가져오기
import pygame      # 게임 개발 도구이지만 이미지 프로세스 또는 조이스틱 입력, 음악 재생 등의 기능을 별도로 사용가능

# 2. 오디오 파일 경로 설정
file = r'10_오디오파일재생프로그램\1번 안녕하세요.mp3'

# 3. 초기화
pygame.init()

# 4. 오디오 파일 로드
pygame.mixer.music.load(file)

# 5. 재생
pygame.mixer.music.play()

# 6. 재생이 끝날 때까지 대기
while pygame.mixer.music.get_busy():
    continue

# 7. 종료
pygame.quit()
