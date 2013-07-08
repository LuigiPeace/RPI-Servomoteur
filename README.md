 ____    ____    ______      ____                                                       __                           
/\  _`\ /\  _`\ /\__  _\    /\  _`\                                                    /\ \__                        
\ \ \L\ \ \ \L\ \/_/\ \/    \ \,\L\_\     __   _ __   __  __    ___     ___ ___     ___\ \ ,_\    __   __  __  _ __  
 \ \ ,  /\ \ ,__/  \ \ \     \/_\__ \   /'__`\/\`'__\/\ \/\ \  / __`\ /' __` __`\  / __`\ \ \/  /'__`\/\ \/\ \/\`'__\
  \ \ \\ \\ \ \/    \_\ \__    /\ \L\ \/\  __/\ \ \/ \ \ \_/ |/\ \L\ \/\ \/\ \/\ \/\ \L\ \ \ \_/\  __/\ \ \_\ \ \ \/ 
   \ \_\ \_\ \_\    /\_____\   \ `\____\ \____\\ \_\  \ \___/ \ \____/\ \_\ \_\ \_\ \____/\ \__\ \____\\ \____/\ \_\ 
    \/_/\/ /\/_/    \/_____/    \/_____/\/____/ \/_/   \/__/   \/___/  \/_/\/_/\/_/\/___/  \/__/\/____/ \/___/  \/_/ 

																			 par http://www.network-science.de/ascii/


Description
===========
Script Python permettant d’interagir avec deux servomoteurs sur deux canals
via le Raspberry Pi et son GPIO.
Les drivers nécessaires sont inclus dans le repo.

Utilisation
===========
Il suffit d'exécuter le script (en ligne de commande) en spécifiant deux
arguments correspondant aux angles en degrés (horizontal puis vertical).
Si tout fonctionne le script s'arrête avec le code 0.

Vous pouvez simplement modifier les "constantes" pour adapter le code à votre
situation (adresse, fréquence, canals, angles).

Exemple
=======
Commande : sudo servomoteur_rpi.py 45 160

Cette commande exécute le script avec un angle horizontal de  45° et
									  un angle vertical   de 160°.

Erreurs
=======
Valeur | Description
     1 | Si les deux arguments requis ne sont par fournis le script s'arrête.
	 2 | Si le nom du script ne correspond pas à celui de la variable
	   | NOM_SCRIPT le script s'arrête.
	 4 | Si au moins l'un des angles n'est pas compris entre 0° et 180° le
	   | script s'arrête.