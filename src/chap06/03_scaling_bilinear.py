import numpy as np, cv2

image = cv2.imread("images/interpolation.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")

size = (350, 400)

dst1 = cv2.resize(image, size, interpolation=cv2.INTER_NEAREST)  # 최근접 이웃 보간법
dst2 = cv2.resize(image, size, interpolation=cv2.INTER_LINEAR)  # 양선형 보간법
dst3 = cv2.resize(image, size, interpolation=cv2.INTER_CUBIC)  # 3차 회선 보간법

cv2.imshow("image", image)
cv2.imshow("OpenCV - Nearest", dst1)
cv2.imshow("OpenCV - bilinear", dst2)
cv2.imshow("OpenCV - cubic", dst3)

cv2.waitKey(0)
