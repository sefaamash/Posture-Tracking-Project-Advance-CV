"""import cv2 as cv
import time
import mediapipe as mp
# Capture video from file

cap=cv.VideoCapture("video 2.mp4")
pTime=0
myPose=mp.solutions.pose
pose=myPose.Pose()
mpDraw=mp.solutions.drawing_utils

while True:
    ret, img = cap.read()
    #mediapipe uses rgb so by default it is BGR so we convert it
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    result=pose.process(imgRGB)
    #to get landmarks of poses .pose_landmarks
    print(result.pose_landmarks)
    if result.pose_landmarks:#if landmarks detected
       mpDraw.draw_landmarks(img, result.pose_landmarks, myPose.POSE_CONNECTIONS)#draw landmarks
       for id, lm in enumerate(result.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv.circle(img, (cx, cy), 5, (255, 0, 0), cv.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, str(int(fps)), (70, 50), cv.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    if ret:    
        cv.imshow("Image", img) 
        if cv.waitKey(20) & 0xFF==ord('d'):
            break   
    else:
            break

cap.release()
cv.destroyAllWindows()
   
  


"""

from configparser import Interpolation
import cv2 as cv
import time
import mediapipe as mp
# Capture video from file
address="https://192.168.1.100:8080/video"
cap=cv.VideoCapture('video 2.mp4')
pTime=0
myPose=mp.solutions.pose
pose=myPose.Pose()
mpDraw=mp.solutions.drawing_utils
def rescale(frame,scale=0.3):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(height,width)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
    
while True:
    ret, img = cap.read()
    frame_resized=rescale(img)
    #mediapipe uses rgb so by default it is BGR so we convert it
    imgRGB=cv.cvtColor(frame_resized,cv.COLOR_BGR2RGB)
    result=pose.process(imgRGB)
    #to get landmarks of poses .pose_landmarks
    print(result.pose_landmarks)
    if result.pose_landmarks:#if landmarks detected
       mpDraw.draw_landmarks(frame_resized, result.pose_landmarks, myPose.POSE_CONNECTIONS)#draw landmarks
       for id, lm in enumerate(result.pose_landmarks.landmark):
            h, w, c = frame_resized.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv.circle(frame_resized, (cx, cy), 5, (255, 0, 0), cv.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(frame_resized, str(int(fps)), (70, 50), cv.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    if ret:    
        cv.imshow("Image", frame_resized) 
        if cv.waitKey(20) & 0xFF==ord('d'):
            break   
    else:
            break

cap.release()
cv.destroyAllWindows()
   