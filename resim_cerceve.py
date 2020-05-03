import cv2
import numpy as np 
from matplotlib import pyplot as plt

mavi=[0,0,255]
img =cv2.imread('/home/oguzhan/Masaüstü/İmage Processing My Codes/messi.jpg')

replicate=cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_REPLICATE)
reflect=cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_REFLECT)
wrap=cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_WRAP)
costant=cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_CONSTANT,value=mavi)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('orijinal')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('reflect')
plt.subplot(234),plt.imshow(wrap,'gray'),plt.title('wrap')
plt.subplot(235),plt.imshow(costant,'gray'),plt.title('constant')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
