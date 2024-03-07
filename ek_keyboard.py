# Imporation des librairie nécessaire
import cv2 as cv 
import keyboard as key
import time
from djitellopy import Tello


qrd = cv.QRCodeDetector()


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

cap = cv.VideoCapture(0)

#def take_off():    # Wake up, cette fonction permet de lancer  la lecture video de la webcam et de resize l'image    
#    while True:
#        ret, frame = cap.read()
#        #img = img.get_frame_read().frame
#        img = cv.flip(frame, 1)
        #img = cv.resize(img, (780,420))
        #img, info = findFace(img)
        #pError = trackFace(info, w, pid, pError)
        #print("center", info[0], "Area", info[1])
#        cv.imshow("Output", img)
#        if key.is_pressed('q'):
#            land()


# Fonction qui permet de se connecter au Tello et de le faire decoller
def wake_up():
    me.takeoff()
    time.sleep(2)
    print ("Tello waked-up")

# Fonction de lecture vidéo
def stream():
    me.streamon()
    while True:
        img = me.get_frame_read().frame
        img = cv.flip(img,1)
        cv.imshow("Output", img)
        if cv.waitKey(10) & 0xFF == ord('q'):
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
    print("Tello moved forward")
    me.send_rc_control()

def move_right():
    me.send_rc_control(20,0,0,0)
    time.sleep(2)
    print("Tello moved right")

def move_left():
    me.send_rc_control(-20,0,0,0)
    time.sleep(2)
    print("Tello moved left")
    
#print("Voici notre premier test avec le keyboard et l'enregistrement de video")
print("En attente de commande !")

while True:
    if key.is_pressed('w'):
        wake_up()
    elif key.is_pressed('s'):
        stream()
    elif key.is_pressed('z'):
        forward()
    elif key.is_pressed('d'):
        move_right()
    elif key.is_pressed('q'):
        move_left()
    elif key.is_pressed('e'):
        land()    
        break

