import cv2


img1 = cv2.imread("./images/test072601.jpg",cv2.IMREAD_GRAYSCALE)

print(len(img1),len(img1[0]))
print(img1.shape)
cv2.line(img1,(0,0),(511,511),(255,0,0),5)
cv2.rectangle(img1,(384,0),(510,128),(0,255,0),3)
cv2.namedWindow("test",cv2.WINDOW_NORMAL)
cv2.imshow("test", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('test.png',img1)