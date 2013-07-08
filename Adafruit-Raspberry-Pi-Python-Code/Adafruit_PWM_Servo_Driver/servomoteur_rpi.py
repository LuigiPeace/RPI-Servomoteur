#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time, sys


#
# Declaration de fonctions
#

# Initialise l'appareil PWM selon l'adresse, la frequence et le mode (debug ou non)
# defini lors de l'appelle de la fonction.
def initPWM(adr, freq, d):
	global PWM
	PWM = PWM(adr, d)
	PWM.setPWMFreq(freq)

# Cette fonction permet de modifier l'angle (en degre) du servomoteur selon l'axe
# choisi : True horizontal & False vertical.
def setAngle(axe, angle_h):
	angle = angleToPulse(angle_h)
	
	global PWM
	
	if axe == True:
		PWM.setPWM(HORIZONTAL, 0, angle)
	else:
		PWM.setPWM(VERTICAL, 0, angle)

# Cette fonction retourne la valeur de l'angle en un nombre correspondant a une pulsation
# d'apres la definition de l'appareil PWM qui est code sur 12 bits (4096 max).
# La valeur par defaut est un angle de 90 degres soit la moitie.
# Elle retourne le nombre correspondant a l'angle par defaut si l'angle n'est pas compris
# entre 0 et 180 degres.
def angleToPulse(angle = 90):
	pulse = ANGLE_DEFAUT
	
	if angle >= 0 and angle <= 180:
		pulse = angle * ANGLE_DELTA / angle_max + ANGLE_MIN
	
	return pulse




#
# Declaration de variables "constantes"
#

# Frequence
FREQUENCE = 60

# Canals
HORIZONTAL = 15
VERTICAL = 14

# Adresse
ADRESSE = 0x40

# Angles (coder sur 12 bits pour PWM)
ANGLE_DEFAUT = 410
ANGLE_MIN = 140
ANGLE_MAX = 680
ANGLE_DELTA = ANGLE_MAX - ANGLE_MIN

# Angles (en degre)
angle_max = 180

angle_h = 90
angle_v = 90

# Nom du script
NOM_SCRIPT = "servomoteur_rpi"



#
# Declaration de variables globales
#

# Erreur
ERREUR = 0
# 1 : nombre d'arguments du script incorrect.
# 2 : premier argument du script ne correspond pas au nom definit.
# 4 : les angles passes en arguments du script sont invalides.

# Appareil PWM
PWM



#
# DEBUT DU PROGRAMME
#

# Verifie le nombre d'arguments
if len(sys.argv) != 3:
	sys.exit(ERREUR = 1)

# Verifie que le nom du script apparait dans le premier argument
if sys.argv[0].count(NOM_SCRIPT) != 1:
	sys.exit(ERREUR = 2)

# Recupere les angles horizontal & vertical (en degre) et les converties en entier
angle_h = int(sys.argv[1])
angle_v = int(sys.argv[2])

# Verifie que les angles sont valides
if angle_h < 0 or angle_h > 180 or angle_v < 0 or angle_v > 180:
	sys.exit(ERREUR = 4)

# Initialise l'appareil PWM
initPWM(ADRESSE, FREQUENCE, True)

# Modifie les angles du servomoteur
setAngle(True, angle_h)
setAngle(False, angle_v)

# Quitte avec comme code d'erreur 0
sys.exit(ERREUR)

#
# FIN DU PROGRAMME
#