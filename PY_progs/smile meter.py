import random , cv2,time
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade=cv2.CascadeClassifier("smile.xml")
video = cv2.VideoCapture(0)
num=0
def smile_meter(frame,x1,y1):
    global num
    if num>4000:
        x=str(random.randint(0,100))
        font=cv2.FONT_HERSHEY_SIMPLEX
        color=(255,0,255)
        text=cv2.putText(frame,"your smile is",(int(x1)+15,int(y1)-70),font,1,color,4,cv2.LINE_AA)
        text=cv2.putText(frame,x+" %",(int(x1)+50,int(y1)-20),font,1,color,4,cv2.LINE_AA)
        time.sleep(15)
        nm=0
        return num
    else:
        