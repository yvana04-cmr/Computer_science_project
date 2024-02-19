import cv2
import numpy as np

# Charger l'image en couleurs
image_couleurs = cv2.imread("Cameroun.png")

# Séparer les canaux de couleur
b, g, r = cv2.split(image_couleurs)

# Appliquer l'égalisation d'histogramme à chaque canal séparément
b_equ = cv2.equalizeHist(b)
g_equ = cv2.equalizeHist(g)
r_equ = cv2.equalizeHist(r)

# Fusionner les canaux égalisés
image_egalisee_couleurs = cv2.merge((b_equ, g_equ, r_equ))

# Afficher les images
cv2.imshow("Image Originale en Couleurs", image_couleurs)
cv2.imshow("Image Égalisée en Couleurs", image_egalisee_couleurs)

cv2.waitKey(0)
cv2.destroyAllWindows()
