import cv2


img1 = cv2.imread("./images/test072601.jpg",cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("test",cv2.WINDOW_NORMAL)
cv2.imshow("test", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('test.png',img1)