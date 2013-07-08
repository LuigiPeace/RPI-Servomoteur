Raspberry Pi - Servomoteur ![Logo du Raspberry Pi](/RPI.png)
==========================

Description
===========
Script Python permettant d’interagir avec deux servomoteurs sur deux canals
via le Raspberry Pi et son GPIO.
Les drivers nécessaires sont inclus dans le repo.

Matériel concerné : Adafruit PCA9685 16-Channel PWM Servo Driver

Utilisation
===========
Il suffit d'exécuter le script (en ligne de commande) en spécifiant deux
arguments correspondant aux angles en degrés (horizontal puis vertical).
Si tout fonctionne le script s'arrête avec le code 0.

Un troisième argument (facultatif) peut être ajouter pour passer en mode debug
qui est désactivé par défaut. (1 = on, 0 = off).

Vous pouvez simplement modifier les "constantes" pour adapter le code à votre
situation (adresse, fréquence, canals, angles).

Exemple
=======
Commande : sudo servomoteur_rpi.py 45 160

Cette commande exécute le script avec un angle horizontal de 45° et un angle
vertical de 160°.

Erreurs
=======
Si une erreur est rencontrée le script s'arrête et retourne un code erreur :

<table>
	<tr>
		<td>Code erreur</td>
		<td>Description</td>
	</tr>
	
	<tr>
		<td>1</td>
		<td>Si les deux arguments requis ne sont par fournis le script s'
			arrête.</td>
	</tr>
	
	<tr>
		<td>2</td>
		<td>Si le nom du script ne correspond pas à celui de la variable
			NOM_SCRIPT le script s'arrête.</td>
	</tr>
	
	<tr>
		<td>4</td>
		<td>Si au moins l'un des angles n'est pas compris entre 0° et 180° le
			script s'arrête.</td>
	</tr>
</table>