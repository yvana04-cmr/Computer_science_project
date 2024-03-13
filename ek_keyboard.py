# Imporation des librairie nécessaire
from djitellopy import Tello
import cv2 as cv 
import keyboard as key
import time
#import face_detection_test1



##################################################
#Connection to tello
me = Tello()
me.connect()
me.left_right_velocity = 0
me.for_back_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0
##################################################

print(me.get_battery())

# Fonction qui permet de se connecter au Tello et de le faire decoller
def wake_up():
    me.takeoff()
    time.sleep(1)
    me.send_rc_control(0, 20, 0, 0)
    time.sleep(0.5)
    me.send_rc_control(0, 0, 0, 0)
    print ("Tello waked-up")

# Fonction de lecture vidéo
def det_tracking():
    # Charger le classificateur Haar cascade pour la détection de visages
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

    me.streamon()
    while True:
        #me.send_rc_control(0,0,20,0)
        #time.sleep(1)
        me.send_rc_control(0,0,0,0)

        #me.send_rc_control(0,10,0,0)
        img = me.get_frame_read().frame
        img = cv.flip(img,1)
        #if not img:
        #    break
        # Convertir l'image en niveaux de gris
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        #me.send_rc_control(5,5,0,0)
        # Détecter les visages dans l'image
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Dessiner des rectangles autour des visages détectés
        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            nombre_visages += len(faces)

        cv.imshow("Output", img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

# Fonction qui coupe le stream de la vidéo de ma webcam
def land():
    me.send_rc_control(0,0,0,0)
    time.sleep(1)
    me.land()

# fonctions permettant le déplacement du drône
def forward():
    me.send_rc_control(0,20,0,0)
    time.sleep(2)
    me.send_rc_control(0, 0, 0, 0)
    print("Tello moved forward")
    

def move_right():
    me.send_rc_control(20, 0, 0, 0)
    time.sleep(2)
    me.send_rc_control(0, 0, 0, 0)
    print("Tello moved right")

def move_left():
    me.send_rc_control(-20,0,0,0)
    time.sleep(2)
    me.send_rc_control(0, 0, 0, 0)
    print("Tello moved left")

def face_tracking():
    me.send_rc_control(0, 0, 0, 0)
    print("The tello drone is supposed right now to track differents faces en store in in a database")
    
#print("Voici notre premier test avec le keyboard et l'enregistrement de video")
print("En attente de commande !")

while True:
    if key.is_pressed('w'):
        wake_up()
    elif key.is_pressed('z'):
        forward()
    elif key.is_pressed('d'):
        move_right()
    elif key.is_pressed('q'):
        move_left()
    elif key.is_pressed('e'):
        land() 
    elif key.is_pressed('space'):
        key.add_hotkey('enter', det_tracking)
        key.wait('esc')   
        break

