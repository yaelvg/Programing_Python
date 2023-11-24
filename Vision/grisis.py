import cv2
import numpy as np

img = cv2.imread("lenna.ppm")
h,w,c = img.shape #informacion de la imagen
#print(h,w,c)

gris = np.zeros((h,w), np.uint8)
for i in range(0,h):
    for x in range(0,w):
        # * CHANELS
        b=img[i,x,0]
        g=img[i,x,1]
        r=img[i,x,2]
        
        gris[i,x] = np.clip((r/3+g/3+b/3), 0, 255)

cv2.imshow("BN", img)
cv2.imshow("bn",gris)
cv2.waitKey()
cv2.destroyAllWindows()