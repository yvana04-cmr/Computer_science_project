import cv2 as cv
import unittest
from djitellopy import Tello


me = Tello()
me.connect()
me.left_right_velocity = 0
me.for_back_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0


def detecter_visages():
    # Charger le classificateur Haar cascade pour la détection de visages
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Ouvrir la capture vidéo
    #cap = cv.VideoCapture(0)

    nombre_visages = 0

    #while(cap.isOpened()):
    while True:
        # Lire une image de la vidéo
        img,ret = me.get_frame_read().frame
        img = cv.flip(img,1)
        if not ret:
            break

        # Convertir l'image en niveaux de gris
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Détecter les visages dans l'image
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        nombre_visages += len(faces)

        # Dessiner des rectangles autour des visages détectés
        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Afficher l'image avec les visages détectés
        cv.imshow('frame', img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # Libérer la capture vidéo et fermer les fenêtres OpenCV
   
    cv.destroyAllWindows()

    return nombre_visages

# Test unitaire pour la fonction de détection de visages
class TestDetecterVisages(unittest.TestCase):
    def test_detecter_visages(self):
        nombre_visages = detecter_visages()
        self.assertGreater(nombre_visages, 0, "Aucun visage détecté")

if __name__ == '__main__':
    # Exécuter le test unitaire
    unittest.main()
