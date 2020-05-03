import cv2

resim = cv2.imread('/home/oguzhan/Masaüstü/İmage Processing My Codes/cicek.png',0)

cv2.imshow('',resim)
cv2.imwrite('gri.png',resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
