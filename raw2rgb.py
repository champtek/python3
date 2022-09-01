__author__ = 'zhouxiaowei'
from PIL import Image
import cv2
import numpy as np
# a = np.fromfile("RAW8_angle33.raw",np.uint8,4656*3496,"").reshape((4656*3496))
# Image.fromarray(a).save("test.png")
rawdata = open("RAW8_angle3333.raw",'rb').read()
imgSize = (4656,3496)

img = Image.frombytes('L', imgSize, rawdata, 'raw')

img.save("RAW8_angle333.tif")

imge = cv2.imread("D:\python\python3\RAW8_angle333.tif",-1)


hsv = cv2.cvtColor(imge,cv2.COLOR_BayerRG2RGB)

# lower_blue=np.array([110,100,100])#blue
# upper_blue=np.array([130,255,255])
#
# lower_green=np.array([60,100,100])#green
# upper_green=np.array([70,255,255])
#
# lower_red=np.array([0,100,100])#red
# upper_red=np.array([10,255,255])
#
# red_mask=cv2.inRange(hsv,lower_red,upper_red)
# blue_mask=cv2.inRange(hsv,lower_blue,upper_blue)
# green_mask=cv2.inRange(hsv,lower_green,upper_green)
#
# red=cv2.bitwise_and(imge,imge,mask=red_mask)
# green=cv2.bitwise_and(imge,imge,mask=green_mask)
# blue=cv2.bitwise_and(imge,imge,mask=blue_mask)
#
#
# res=green+red+blue



cv2.imshow('img',hsv)

cv2.imwrite("test1111.tif",hsv)
cv2.imwrite("test1111.jpg",hsv)
cv2.waitKey(0)

cv2.destroyAllWindows()