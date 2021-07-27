import cv2

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img1,(x,y),100,(255,0,0),-1)
img1 = cv2.imread("./images/test072601.jpg")

cv2.namedWindow("test",cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img1)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()