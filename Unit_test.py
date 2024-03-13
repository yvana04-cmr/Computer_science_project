import cv2 
import keyboard as key
import time
from djitellopy import Tello
import unittest


class TestTelloFunctions(unittest.TestCase):
    # Initialiser un object comme etant notre drone
    def setUp(self):
        self.me = Tello()
        self.me.connect()
        self.me.streamon()
        time.sleep(2)
    
    def test_wake_up(self):
        self.me.takeoff()
        time.sleep(1)
        self.assertTrue(self.me.is_flying(), "Le Tello n'est pas en vol après le décollage")

    def test_adjust_brightness(self):
        img = cv2.imread("Basketball.jpg")
        brightened_img = adjust_brightness(img, 2.0)
        self.assertGreater(brightened_img.mean(), img.mean(), "Luminosite non augmentée")

    def test_land(self):
        self.me.takeoff()
        time.sleep(1)
        self.me.land()
        self.assertFalse(self.me.is_flying(), "Le Tello est toujours en vol après l'atterrissage")

    def test_forward(self):
        self.me.takeoff()
        time.sleep(1)
        self.me.send_rc_control(0, 20, 0, 0)
        time.sleep(2)
        self.assertEqual(self.me.get_distance_tof(), 100, "La fonction forward n'a pas déplacé le Tello vers l'avant")

    def test_move_right(self):
        self.me.takeoff()
        time.sleep(1)
        self.me.send_rc_control(20, 0, 0, 0)
        time.sleep(2)
        self.assertEqual(self.me.get_distance_tof(), 100, "La fonction move_right n'a pas déplacé le Tello vers la droite")

    def test_move_left(self):
        self.me.takeoff()
        time.sleep(1)
        self.me.send_rc_control(-20, 0, 0, 0)
        time.sleep(2)
        self.assertEqual(self.me.get_distance_tof(), 100, "La fonction move_left n'a pas déplacé le Tello vers la gauche")

    
    #def test_stream(self):
    #    nombre_visages = stream()
    #    self.assertGreater(nombre_visages, 0, "Aucun visage détecté")

def adjust_brightness(image, factor):
    """
    Ajuste la luminosité de l'image en multipliant chaque pixel par un facteur spécifié.
    """
    return cv2.convertScaleAbs(image, alpha=factor, beta=0)

if __name__ == '__main__':
    # Exécuter le test unitaire
    unittest.main()