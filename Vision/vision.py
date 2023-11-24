import cv2
#import matplotlib.pyplot as ptl
# ! Trabaja en BGR

img = cv2.imread("lenna.ppm") # * Realiza la lectura en forma matrizial
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("lenna", img)

cv2.waitKey()
cv2.destroyAllWindows()