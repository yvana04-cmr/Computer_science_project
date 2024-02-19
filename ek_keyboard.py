# Imporation des librairie nécessaire
import cv2 as cv 
import keyboard as key

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
        if cv.waitKey(1) & 0xFF== ord('q'):
            break


def land():
    cap.close()

print("Voici notre premier test avec le keyboard et l'enregistrement de video")
print("En attente de commande !")
 #print(key.is_pressed('ctrl'))
c = key.record() #attente de la commande par pression d'une touche de clavier
if (c == 'o'):
    print('c')
    take_off() # Appel de la focntion take_off si le bouton appuyé est o
elif (c == 'q'):
    land() # Appel de la fonction permettant de metrre fin au processus de capture vidéo