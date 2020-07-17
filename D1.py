import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('big.jpg')
aa=img[100:300,100:300]
bb=img[300:500,300:500]
dst=cv2.addWeighted(aa,0.7,bb,0.3,0)
img[200:400,200:400] = dst
# dst=cv2.addWeighted(img1,0.7,img,0.3,0)
#size要一樣才能混合
 
 
cv2.imshow('rrr',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
# plt.show()


# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# img=cv2.imread('big.jpg')
# cv2.imshow('before',img)
# img1=cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)
# cv2.imshow('after',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 改變色階
