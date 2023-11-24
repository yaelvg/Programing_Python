'''Clase del 24/11/23'''
# * convolucion CNN
# * Entre mañor sea el kernel un mayor de detalle se estara trabajando en imagenes
import cv2
import numpy

img = cv2.imread('lenna.ppm')

h, w, c = img.shape

kernel = numpy.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9] ])
resultado = numpy.zeros((h,w,c), numpy.uint8)
mhk = kernel.shape[0]//2
mwk = kernel.shape[1]//2

for i in range(mhk, h - mhk):
    for j in range(mwk,w - mwk):
        acc = 0
        for ik in range(0, kernel.shape[0]):
            for jk in range(0, kernel.shape[1]):
                acc += (kernel[ik,jk] * img[i-mhk + ik,j - mwk + jk]).astype('uint16')
        
        resultado[i,j] = numpy.clip(acc, 0, 255).astype('uint8')          

cv2.imshow('Lenna', img)
cv2.imshow('Ressss', resultado)
cv2.waitKey()
cv2.destroyAllWindows()