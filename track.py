import cv2
import numpy as np
from pynput.mouse import Button, Controller
#from win32api import GetSystemMetrics
mouse=Controller()

lowerBound=np.array([150,30,40]) # hot pink
upperBound=np.array([170,150,255])

cam= cv2.VideoCapture(0)
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

#app=wx.App(False)
#(sx,sy)=wx.GetDisplaySize()
sx = 1280
sy = 720
(camx,camy)=(320,240)

while True:
    ret, img=cam.read()
    img=cv2.resize(img,(340,220))

    #convert BGR to HSV
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    # create the Mask
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    #morphology
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal=maskClose
    _,conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    print(len(conts))
    if (len(conts) > 0):
      if (len(conts) == 1):
        x,y,w,h=cv2.boundingRect(conts[0])
        if (w * h > 1000):
          mouse.press(Button.left)
          mouseX = int((sx * x) / camx)
          mouseY = int((sy * y) / camy)
          mouse.position= (sx - mouseX, mouseY)
      else:
        count = 0
        for cont in conts:
          x,y,w,h=cv2.boundingRect(cont)
          if (w * h > 1000):
            count += 1
            if (count == 2):
              cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
              mouse.release(Button.left)
              mouseX = int((sx * x) / camx)
              mouseY = int((sy * y) / camy)
              mouse.position= (sx - mouseX, mouseY)
              break
    
    cv2.imshow("cam",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cam.release()
cv2.destroyAllWindows()
