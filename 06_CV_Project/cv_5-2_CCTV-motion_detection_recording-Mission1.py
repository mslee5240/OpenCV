# OpenCV를 사용하여 실시간으로 웹캠에서 움직임을 감지하고, 움직임이 일정 기준 이상 발생하면 녹화를 시작하는 프로그램

############################################################################################################
# 미션 1:
#    - 웹캠에서 실시간으로 움직임을 감지하여 자동으로 녹화를 시작하세요.
#    - 움직임이 감지되면 최소 5초 동안 동영상을 저장하고, 움직임이 멈추면 녹화를 종료하세요.
#    - 각 프레임에 현재 시간을 표시하여 저장된 영상에 타임스탬프를 추가하세요.
#    - 결과:
#        - 움직임 감지 결과(diff)와 현재 시간을 표시한 프레임을 화면에 출력.
#        - 움직임이 감지되면 "녹화 중..." 메시지 출력.
#        - 녹화된 영상 파일은 'Capture' 폴더에 저장 (예: 녹화_YYYY_MM_DD_HH_MM_SS.avi).
#    - 조건:
#        - 연속된 3개의 프레임을 비교하여 움직임 감지 (absdiff 사용).
#        - 움직임 픽셀 수가 특정 임계값(diff_min)을 초과하면 움직임으로 간주.
#        - 타임스탬프는 영상 상단에 표시 (PIL.ImageFont 사용).
#    - 주의:
#        - 녹화 파일명에 타임스탬프를 포함하여 중복되지 않도록 설정.
############################################################################################################

import cv2
import datetime
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import os

# 1. 프레임 비교 함수 정의
def get_diff_img(frame_a, frame_b, frame_c, threshold):
    # 연속된 세 개의 프레임을 비교하여 움직임 감지
    frame_a_gray = cv2.cvtColor(frame_a, cv2.COLOR_BGR2GRAY)
    frame_b_gray = cv2.cvtColor(frame_b, cv2.COLOR_BGR2GRAY)
    frame_c_gray = cv2.cvtColor(frame_c, cv2.COLOR_BGR2GRAY)

    diff_ab = cv2.absdiff(frame_a_gray, frame_b_gray)
    diff_bc = cv2.absdiff(frame_b_gray, frame_c_gray)

    ret, diff_ab_t = cv2.threshold(diff_ab, threshold, 255, cv2.THRESH_BINARY)
    ret, diff_bc_t = cv2.threshold(diff_bc, threshold, 255, cv2.THRESH_BINARY)

    diff = cv2.bitwise_and(diff_ab_t, diff_bc_t)

    k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)

    diff_cnt = cv2.countNonZero(diff)
    return diff, diff_cnt

# 2. 카메라 객체 생성 및 초기화
capt = cv2.VideoCapture(0)
capt.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capt.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 3. 코덱, 폰트, 녹화 상태 변수 초기화
codex = cv2.VideoWriter_fourcc(*'XVID')
font_ = ImageFont.truetype('fonts/SCDream6.otf', 20)
is_record = False
on_record = False
threshold = 40
diff_min = 10
min_cnt_record = 50
cnt_record = 0

# 4. 초기 프레임(1번, 2번) 설정
ret, frame_a = capt.read()
ret, frame_b = capt.read()

# 5. 실행 루프
while True:
    # 5-1. 현재 프레임 읽기
    ret, frame_c = capt.read()

    # 5-2. 현재 시간 계산 및 텍스트용 문자열 생성
    t_now = datetime.datetime.now()
    t_str = t_now.strftime('%Y/%m/%d %H:%M:%S')
    t_str_path = t_now.strftime('%Y_%m_%d_%H_%M_%S')

    # 5-3. 움직임 감지
    diff, diff_cnt = get_diff_img(frame_a=frame_a, frame_b=frame_b, frame_c=frame_c, threshold=threshold)

    # 5-4. 프레임에 현재 시간 텍스트 추가
    frame = frame_c.copy()  # 원본 frame_c를 그대로 복사해서 frame에
    cv2.rectangle(img=frame, pt1=(10, 15), pt2=(340, 35), color=(0, 0, 0), thickness=-1)

    frame_pil = Image.fromarray(frame)
    draw = ImageDraw.Draw(frame_pil)
    draw.text(xy=(10, 15), text="나 안 잔다 " + t_str, font=font_, fill=(255, 255, 255))

    # 🔴 5-4-1. 녹화 중이면 빨간 점 표시
    if is_record:
        draw.ellipse((550, 10, 580, 40), fill=(0, 0, 255))  # 빨간 원 (x0,y0,x1,y1)
    frame = np.array(frame_pil)

    # 5-5. 움직임 감지되면 녹화 시작
    if diff_cnt > diff_min:
        is_record = True
        if on_record == False:
            os.makedirs('Capture', exist_ok=True)  # 폴더 없으면 생성
            video_ = cv2.VideoWriter(f"Capture/녹화_{t_str_path}.avi", codex, 20, (frame.shape[1], frame.shape[0]))
        cnt_record = min_cnt_record

    # 5-6. 녹화 중이면 현재 프레임 저장
    if is_record:
        print("녹화 중...")
        video_.write(frame)  # !!! 여기서 frame (텍스트 들어간거)을 저장해야 합니다!
        cnt_record -= 1
        on_record = True

    # 5-7. 녹화가 끝났으면 상태 초기화
    if cnt_record == 0:
        is_record = False
        on_record = False

    # 5-8. 화면에 표시
    cv2.imshow("diff", diff)
    cv2.imshow("Original", frame)

    # 5-9. 프레임 업데이트
    frame_a = frame_b
    frame_b = frame_c

    # 5-10. 종료 체크
    key = cv2.waitKey(30)
    if key == ord('q'):
        break


# 6. 종료 처리
capt.release()
cv2.destroyAllWindows()
