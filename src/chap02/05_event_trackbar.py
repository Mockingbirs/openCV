import numpy as np
import cv2

def onChage(value):
    global image  # 전역변수

    add_value = value - int(image[0][0])  # 트랙바 값과 영상 화소값 차분
    print('추가 화소값: ', add_value)

    image[:] = image + add_value    # 행렬과 스칼라 덧셈 수행
    cv2.imshow(title, image)

image=np.zeros((300,500), np.uint8)

title = 'Trackbar Event'
cv2.imshow(title, image)

cv2.createTrackbar('Brightness', title, image[0][0], 255, onChage)
cv2.waitKey(0)
cv2.destroyAllWindows(title)


