import cv2
import matplotlib.pyplot as plt

image = cv2.imread("images/matplot.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상 파일 읽기 에러")

rows, cols = image.shape[:2]
rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) ## BGR2RGB : BGR to RGB 라는 의미. BGR의 컬러 공간은 RGB로 바꾸겠다는 거다.
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) ## 흑백 이미지 같은 것.

fig = plt.figure(num=1, figsize=(3, 4))
plt.imshow(image)
plt.title('figure1-original(bgr')
plt.axis('off') ## 축 표시하지 않기.
plt.tight_layout() ## 여백 없애주기.

fig = plt.figure(num=2, figsize=(6, 4))
plt.suptitle('figure2-pyplot image display')
plt.subplot(1, 2, 1)
plt.imshow(rgb_img)
plt.axis([0, cols, rows, 0]) ## 이미지가 딱 그 크기만큼 출력되도록 사이즈를 잡아줌.
plt.title('rgb color')

plt.subplot(1, 2, 2)
plt.imshow(gray_img, cmap='gray')
plt.axis([0, cols, rows, 0])
plt.title('gray_img2')

plt.show()