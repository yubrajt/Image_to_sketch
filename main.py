'''This is the simple and small project that help to convert image into sketch with OpenCV- python'''


import cv2
#between matplotlib and computer vision this is my try on cv2
#image is being read
img = cv2.imread("jibu.JPG")
#inorder to make proper sketch real image should be  grayed, then inverted similarly have to be blurred
grey_filter = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_filter)
blur = cv2.GaussianBlur(invert,(21,21),0)
#image should be invereted blur

invertedblur = cv2.bitwise_not(blur)

#after that gray and inverted blur should be mergeinto one

sketch = cv2.divide(grey_filter,invertedblur,scale=256.0)
#imwrite will save the image in the directory
#cv2.imwrite("Output1.png",sketch)
#imshow will just show the result
cv2.imshow("Output",sketch)
#since image will be gone immedietly so we have writtern wait key

cv2.waitKey()
