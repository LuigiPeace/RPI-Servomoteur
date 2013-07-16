
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

# Cette fonction permet de modifier l'angle (en degres) du servomoteur selon l'axe
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
# entre l'angle minimum et maximum.
def angleToPulse(angle = 90):
	pulse = ANGLE_DEFAUT
	
	if angle >= angle_min and angle <= angle_max:
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
ANGLE_MIN = 150
ANGLE_MAX = 680
ANGLE_DELTA = ANGLE_MAX - ANGLE_MIN

# Angles (en degre)
angle_min = 0
angle_max = 180

angle_h = 90
angle_v = 90

# Nom du script
NOM_SCRIPT = "servomoteur_rpi.py"



#
# Declaration de variables globales
#

# Erreur
ERREUR = 0
# 1 : nombre d'arguments du script incorrect.
# 2 : premier argument du script ne correspond pas au nom definit.
# 4 : les angles passes en arguments du script sont invalides.

# Mode debug
DEBUG = False



#
# DEBUT DU PROGRAMME
#

def main():
	# Verifie le nombre d'arguments (le troisieme argument est facultatif)
	if len(sys.argv) != 3 and len(sys.argv) != 4:
		ERREUR = 1
		return ERREUR

	# Recupere si possible le mode debug
	if len(sys.argv) == 4:
		DEBUG = bool(sys.argv[3])

	# Verifie que le nom du script apparait dans le premier argument
	if sys.argv[0].count(NOM_SCRIPT) != 1:
		if DEBUG == True:
			print "Le nom du script ne correspond a celui declarer dans la variable."
		ERREUR = 2
		return ERREUR

	# Recupere les angles horizontal et vertical (en degres) et les converties en entier
	angle_h = int(sys.argv[1])
	angle_v = int(sys.argv[2])

	# Verifie que les angles sont valides
	if angle_h < angle_min or angle_h > angle_max or angle_v < angle_min or angle_v > angle_max:
		if DEBUG == True:
			print "L'angle horizontal et/ou vertical n'est pas compris entre %d et %d degres." % (angle_min, angle_max)
		ERREUR = 4
		return ERREUR

	# Initialise l'appareil PWM
	initPWM(ADRESSE, FREQUENCE, DEBUG)

	# Modifie les angles du servomoteur
	setAngle(True, angle_h)
	setAngle(False, angle_v)

	# Quitte avec comme code d'erreur 0
	return 0

#
# FIN DU PROGRAMME
#

if __name__ == "__main__":
    sys.exit(main())