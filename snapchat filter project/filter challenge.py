import cv2
import numpy as np
eye_cascade = cv2.CascadeClassifier("../../../../Anaconda3/Lib/site-packages/cv2/data/haarcascade_eye.xml")

# image_path = "Test/Before.PNG"
glasses_path = "Train/glasses.PNG"

# image = cv2.imread(image_path)
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
glasses_image = cv2.imread(glasses_path, cv2.IMREAD_UNCHANGED)

cv2.

# eyes = eye_cascade.detectMultiScale(image, 1.3, 5)
# glasses_image[:,:,3] = np.full((221, 483), 100)
# print(glasses_image[:,:,3])
# image[0:glasses_image.shape[0],0:glasses_image.shape[1]] = glasses_image[:,:377]
# print(image.shape)
# for x,y,w,h in eyes:
# 	cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,255), 2)

cv2.imshow('image', glasses_image[:,:,:3])
cv2.waitKey(0)
cv2.destroyAllWindows()