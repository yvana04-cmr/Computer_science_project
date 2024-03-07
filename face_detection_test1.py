import cv2
import unittest

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

# Test unitaire pour la fonction de détection de visages
class TestDetecterVisages(unittest.TestCase):
    def test_detecter_visages(self):
        nombre_visages = detecter_visages()
        self.assertGreater(nombre_visages, 0, "Aucun visage détecté")

if __name__ == '__main__':
    # Exécuter le test unitaire
    unittest.main()
