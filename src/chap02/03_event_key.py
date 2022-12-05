import numpy as np
import cv2

# switch case 문을 dictionary으로 구현

switch_case = {
    ord('a'):"a키 입력",   #ord() 함수 - 문자를 아스키코드로 변환
    ord('b'):"b키 입력",
    0x41:'A키 입력',
    int('0x42', 16):'B키 입력',
    37:'왼쪽 화살표키 입력',  # 2424832  0x250000
    38:'윗쪽 화살표키 입력', # 2490368 0x260000
    39:'오른쪽 화살표키 입력', # 2555904 0x270000
    40:'아래쪽 화살표키 입력' # 2621440 0x280000
}

image = np.ones((200,300), np.float64)
cv2.namedWindow('keyboard Event')
cv2.imshow('keyboard Event', image)

while True:
    key = cv2.waitKeyEx(100)
    if key ==27:
        break        # ESC키 누르면 종료

    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()