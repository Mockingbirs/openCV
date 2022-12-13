import numpy as np, cv2
from Common.utils import contain
from Common.interpolation import bilinear_value


def rotate(img, degree):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = (degree/180) * np.pi
    sin, cos = np.sin(radian), np.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            y = -j * sin + i * cos
            x = j * cos + i * sin

            if contain((y,x),img.shape):
                dst[i, j] = bilinear_value(img, [x, y])

    return dst

image = cv2.imread("images/rotate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")

dst1 = rotate(image, 15)
dst2 = rotate(image, 30)



cv2.imshow("image", image)
cv2.imshow("dst1-15", dst1)
cv2.imshow("dst2-30", dst2)

cv2.waitKey(0)