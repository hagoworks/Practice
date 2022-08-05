import os
import cv2
import numpy as np

IMG_PATH = "../images"
IMG_PATH = "c:\Temp\py\opencv\images"

if __name__ == "__main__":
    img = cv2.imread(os.path.join(IMG_PATH, "logo.png"))
    
    h, w, _ = img.shape
    
    # Resize
    shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    zoom2 = cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    
    cv2.imshow("Original", img)
    cv2.imshow("Shrink", shrink)
    cv2.imshow("Zoom2", zoom2)
    
    # Move
    M = np.float32([[1, 0, 10],[0, 1, 20]])
    move = cv2.warpAffine(img, M, (h,w))
    cv2.imshow("Translation", move)
    
    #Rotation
    M = cv2.getRotationMatrix2D((w /2, h /2), 90, 0.5)
    rotation = cv2.warpAffine(img, M, (w, h))
    cv2.imshow("Translotaion", rotation)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()