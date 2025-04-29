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
import time
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import os

# 1. 폴더 생성
os.makedirs("Capture", exist_ok=True)
os.makedirs("Record", exist_ok=True)

# 2. 프레임 비교 함수
def get_diff_img(frame_a, frame_b, frame_c, threshold):
    frame_a_gray = cv2.cvtColor(frame_a, cv2.COLOR_BGR2GRAY)
    frame_b_gray = cv2.cvtColor(frame_b, cv2.COLOR_BGR2GRAY)
    frame_c_gray = cv2.cvtColor(frame_c, cv2.COLOR_BGR2GRAY)

    diff_ab = cv2.absdiff(frame_a_gray, frame_b_gray)
    diff_bc = cv2.absdiff(frame_b_gray, frame_c_gray)

    _, diff_ab_t = cv2.threshold(diff_ab, threshold, 255, cv2.THRESH_BINARY)
    _, diff_bc_t = cv2.threshold(diff_bc, threshold, 255, cv2.THRESH_BINARY)

    diff = cv2.bitwise_and(diff_ab_t, diff_bc_t)

    k = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    diff = cv2.morphologyEx(diff, cv2.MORPH_OPEN, k)

    diff_cnt = cv2.countNonZero(diff)
    return diff, diff_cnt

# 3. 카메라 초기화
capt = cv2.VideoCapture(0)
capt.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capt.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 4. 폰트 및 감지 기준 설정
font = ImageFont.truetype('fonts/SCDream6.otf', 20)
threshold = 40
diff_min = 10
fps = 30

# 5. 초기 프레임 설정
ret, frame_a = capt.read()
ret, frame_b = capt.read()

is_recording = False
record_start_time = None
video_writer = None

# 6. 루프 시작
while True:
    ret, frame_c = capt.read()
    frame_for_display = np.array(frame_c)

    t_now = datetime.datetime.now()
    t_str = t_now.strftime('%Y/%m/%d %H:%M:%S')
    t_str_path = t_now.strftime('%Y_%m_%d_%H_%M_%S')

    diff, diff_cnt = get_diff_img(frame_a, frame_b, frame_c, threshold)

    # 텍스트 삽입
    frame_pil = Image.fromarray(frame_for_display)
    draw = ImageDraw.Draw(frame_pil)
    draw.rectangle([(10, 15), (400, 35)], fill=(0, 0, 0))  # 넉넉하게 배경
    draw.text((10, 15), f"보고있다~ {t_str}", font=font, fill=(255, 255, 255))
    frame_with_text = np.array(frame_pil)

    # 움직임 감지되었고, 아직 녹화 중이 아니면 녹화 시작
    if diff_cnt > diff_min and not is_recording:
        print("움직임 감지! 녹화 시작")
        is_recording = True
        record_start_time = time.time()

        # 녹화 파일 만들기
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        video_filename = f"Capture/recorded_{t_str_path}.avi"
        video_writer = cv2.VideoWriter(video_filename, fourcc, fps, (frame_with_text.shape[1], frame_with_text.shape[0]))

    # 녹화 중이면 비디오 파일에 현재 프레임 저장
    if is_recording:
        video_writer.write(frame_with_text)

        # 5초(=5.0초) 경과하면 녹화 종료
        if time.time() - record_start_time >= 5.0:
            print("5초 녹화 완료. 저장 종료.")
            is_recording = False
            video_writer.release()

    # 화면 출력
    cv2.imshow("Original", frame_with_text)
    cv2.imshow("diff", diff)

    # 프레임 업데이트
    frame_a = np.array(frame_b)
    frame_b = np.array(frame_c)

    key = cv2.waitKey(30)
    if key == ord('q'):
        break

# 종료
capt.release()
if video_writer is not None and video_writer.isOpened():
    video_writer.release()
cv2.destroyAllWindows()
