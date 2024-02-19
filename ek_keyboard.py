# Imporation des librairie nécessaire
import cv2 as cv 
import keyboard as key
import time

#char c

cap = cv.VideoCapture(0)

def take_off():    # Wake up, cette fonction permet de lancer  la lecture video de la webcam et de resize l'image    
    while True:
        ret, frame = cap.read()
        #img = img.get_frame_read().frame
        img = cv.flip(frame, 1)
        #img = cv.resize(img, (780,420))
        #img, info = findFace(img)
        #pError = trackFace(info, w, pid, pError)
        #print("center", info[0], "Area", info[1])
        cv.imshow("Output", img)
        if key.is_pressed('q'):
            land()


def land():
    cap.release()
    cv.destroyAllWindows()

print("Voici notre premier test avec le keyboard et l'enregistrement de video")
print("En attente de commande !")
 #print(key.is_pressed('ctrl'))
#c = key.is_pressed() #attente de la commande par pression d'une touche de clavier

while True:
    if key.is_pressed('t'):
        take_off()
        break




