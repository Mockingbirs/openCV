import numpy as np , cv2, time


# 직접 ,  opencv , numpy 를 활용한 접근 방법

def pixel_access1(image):
    image1 = np.zeros(image.shape[:2],image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i, j]
            image1[i, j] = 255 - pixel
    return image1

def pixel_access2(image):
    image2 = np.zeros(image.shape[0:2], image.dtype)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image.item(i, j)
            image2.itemset((i,j), 255-pixel)
    return image2

def pixel_access3(image):
    lut = [255 - i for i in range(256)]  # lookup 테이블 생성
    lut = np.array(lut, np.uint8)
    image3 = lut[image]
    return image3

def pixel_access4(image):
    image4 = cv2.subtract(255, image)
    return image4

def pixel_access5(image):
    image5 = 255 - image
    return image5

image =cv2.imread("images/bright.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류 발생")

# 수행 시간 체크
def time_check(func, msg):
    start_time = time.perf_counter()
    ret_img = func(image)
    elaped = (time.perf_counter() - start_time) * 1000
    print(msg, "수행 시간 : %.2f ms" % elaped)
    return ret_img

image1 = time_check(pixel_access1, "[방법1] 직접 접근 방식")
image2 = time_check(pixel_access2, "[방법2] item() 함수 방식")
image3 = time_check(pixel_access3, "[방법3] 룩업테이블 방식")
image4 = time_check(pixel_access4, "[방법4] OpenCV 방식")
image5 = time_check(pixel_access5, "[방법5] ndarray 연산 방식")

# 결과 영상 보기
cv2.imshow("image - original", image)
cv2.imshow("image1 - directly access", image1)
cv2.imshow("image2 - item()/itemset()", image2)
cv2.imshow("image3 - LUT", image3)
cv2.imshow("image4 - OpenCV", image4)
cv2.imshow("image5 - ndarray", image5)

cv2.waitKey(0)