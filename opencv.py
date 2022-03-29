import cv2

fixedPath = 'fused.jpg'
image = cv2.imread(fixedPath, 0)
cv2.imshow("Zamasu", image)
cv2.waitKey(0)
cv2.destroyAllWindows()