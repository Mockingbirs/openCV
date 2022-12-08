import numpy as np, cv2, time

def blur_convolution(image, filter):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    xcenter, ycenter = filter.shape[1]//2, filter.shape[0]//2

    for i in range(ycenter, rows - ycenter):
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1 ## 관심영역에 대한 범위를 지정해주고 있는 것이다. 처음에 0부터 시작해서 1로 가는 값이라고 하는데...?
            x1, x2 = j - xcenter, j + xcenter + 1 ## 1, 3이 저장되어 있다고 생각하면 된다고 하시는데...?
            roi = image[y1:y2, x1:x2].astype("float32") ## roi : 원본이미지에서 우리가 관심을 가지는 부분을 말한다.

            tmp = cv2.multiply(roi, filter)
            dst[i, j] = cv2.sumElems(tmp)[0]

    return dst

image = cv2.imread("images/filter_blur.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류 발생")

# 블러링 마스크 원소 지정
filter = [1/9, 1/9, 1/9,
        1/9, 1/9, 1/9,
        1/9, 1/9, 1/9]

mask = np.array(filter, np.float32).reshape(3, 3)
blur = blur_convolution(image, mask)

cv2.imshow("image", image)
cv2.imshow("blur", blur.astype('uint8'))
cv2.waitKey(0)
