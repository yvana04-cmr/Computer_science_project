# Imporation des librairie nécessaire
import cv2 as cv 
from djitellopy import Tello
import keyboard as key
import time

#char c

cap = cv.VideoCapture(0)
# Wake up, cette fonction permet de lancer  la lecture video de la webcam et de resize l'image    
def action():
    while True:
        ret, frame = cap.read()
        #img = img.get_frame_read().frame
        if not ret:
            print("Erreur lors de la lecture de la webcam.")
            break
        img = cv.flip(frame, 1)
        #img = cv.resize(img, (780,420))
        #img, info = findFace(img)
        #pError = trackFace(info, w, pid, pError)
        #print("center", info[0], "Area", info[1])
        cv.imshow("Output", img)
        if cv.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

while True:
    if key.is_pressed('a'):
        print("On espère mon petit que ca marche comme tu le souhaites !")
    elif key.is_pressed('space'):
        key.add_hotkey('enter', action)
        key.wait('esc')
        break 