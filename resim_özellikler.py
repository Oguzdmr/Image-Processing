import cv2
import numpy as np 


img = cv2.imread('/home/oguzhan/Masaüstü/İmage Processing My Codes/messi.jpg')

img[:,:,1]=0

cv2.imshow('messi', img)

cv2.waitKey(0)
cv2.destroyAllWindows()