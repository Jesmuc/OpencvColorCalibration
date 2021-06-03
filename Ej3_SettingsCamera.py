import cv2
import numpy as np
import keyboard

cap = cv2.VideoCapture(0)

width=320
height=240
#cap.set(3,width)#320
#cap.set(4,height)#240
#get actual parameters: #default value
width_d=cap.get(3) #640
height_d=cap.get(4)#480
fps=cap.get(cv2.CAP_PROP_FPS)#30
a10=cap.get(10) #brightness 128.0
a11=cap.get(11) #contrast 32.0
a12=cap.get(12) #saturation 32.0
a13=cap.get(13) #hue -1.0
a14=cap.get(14) #gain 131.0
a15=cap.get(15) #exposure -6
a23=cap.get(23) #temperature 1070.0 or 4460 or 4300
a27=cap.get(27) #zoom -1.0
a28=cap.get(28) #focus -1.0
a45=cap.get(45) #WB temperature -1.0
a40=cap.get(40) #sample aspect ratio (num) 1.0
a41=cap.get(41) #sample aspect ratio (den) 1.0
a26=cap.get(26) #white balance red -1.0
a21=cap.get(21) #autoexposure 1
a39=cap.get(39) #AUTOFOCUS -1.0
a44=cap.get(44) #AUTO_WB # -1.0
a6=cap.get(6)#4-character code of codec 20.0
v4l_support=cap.get(cv2.CAP_V4L) # -1.0
v4l2_support=cap.get(cv2.CAP_V4L2) # -1.0
print("width:",width_d,"height:",height_d,"fps:",fps,"brightness:",a10, "codec:",a6)
print("v4l_support:",v4l_support,"v4l2_support:",v4l2_support,"contrast:",a11,"saturation:",a12,"hue:",a13,"gain:",a14,"exposure:",a15)
print("temperature:",a23,"zoom:",a27,"focus:",a28,"WB temp:",a45,"sar(num):",a40)
print("sar(den):",a41,"WB red:",a26,"AutoExp:",a21,"AutoFocus:",a39,"AutoWB:",a44)

while(True):
    ret, frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xff == ord("q"): 
        print("You pressed stop!")
        break
    if keyboard.is_pressed("q"):
        print("You pressed stop!")
        break
cap.release()
cv2.destroyAllWindows()