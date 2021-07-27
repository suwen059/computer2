import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('car.jpg')
rows,cols,ch = img.shape
# 左图中画面中的点的坐标 四个
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
# 变换到新图片中，四个点对应的新的坐标 一一对应
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

# 生成变换矩阵
M = cv2.getPerspectiveTransform(pts1,pts2)
# 进行透视变换
dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()