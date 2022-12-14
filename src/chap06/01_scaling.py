import numpy as np, cv2

def scaling(img, size): # 크기 변경 함수
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])

    y = np.arange(0, img.shape[0], 1)
    x = np.arange(0, img.shape[1], 1)

    y, x = np.meshgrid(y, x)
    i, j = np.int32(y * ratioY), np.int32(x * ratioX)
    dst[i, j] = img[y, x]

    return dst

image = cv2.imread("images/scaling.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")

dst1 = scaling(image, (150, 200))  # 크기 축소
dst2 = scaling(image, (300, 400))  # 크기 확대

cv2.imshow("image", image)
cv2.imshow("dst1 - zoom in", dst1)
cv2.imshow("dst2 - zoom out", dst2)

cv2.waitKey(0)