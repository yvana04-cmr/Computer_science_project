# Imporation des librairie nécessaire
import cv2 
import keyboard as key
import time
from djitellopy import Tello
import unittest

qrd = cv2.QRCodeDetector()


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

# cap = cv.VideoCapture(0)
def detecter_visages():
    # Charger le classificateur Haar cascade pour la détection de visages
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Ouvrir la capture vidéo
    cap = cv2.VideoCapture(0)

    nombre_visages = 0

    while(cap.isOpened()):
        # Lire une image de la vidéo
        ret, frame = cap.read()
        if not ret:
            break

        # Convertir l'image en niveaux de gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Détecter les visages dans l'image
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        nombre_visages += len(faces)

        # Dessiner des rectangles autour des visages détectés
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Afficher l'image avec les visages détectés
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



    # Libérer la capture vidéo et fermer les fenêtres OpenCV
    cap.release()
    cv2.destroyAllWindows()

    return nombre_visages

# Fonction qui permet de se connecter au Tello et de le faire decoller
def wake_up():
    me.takeoff()
    time.sleep(1)
    me.send_rc_control(0, 20, 0, 0)
    time.sleep(0.5)
    me.send_rc_control(0, 0, 0, 0)
    print ("Tello waked-up")

# Fonction de lecture vidéo
def stream():
    me.streamon()
    while True:
        img = me.get_frame_read().frame
        img = cv2.flip(img,1)
        cv2.imshow("Output", img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
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
    elif key.is_pressed('space'):
        key.add_hotkey('enter', face_tracking)   
        break


# tests unitaires
    # Test unitaire pour la fonction de détection de visages
class TestDetecterVisages(unittest.TestCase):
    def test_detecter_visages(self):
        nombre_visages = detecter_visages()
        self.assertGreater(nombre_visages, 0, "Aucun visage détecté")

if __name__ == '__main__':
    # Exécuter le test unitaire
    unittest.main()