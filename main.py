import cv2
filePath = 'kenma.jpg'
imgFlag = int (1)
img = cv2.imread(filePath,imgFlag)
cv2.imshow("boyfiee",img)
cv2.waitkey(0)
cv2.destroyAllWindows() 