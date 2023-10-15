import sys
import math

def conversion_radian(valeur):
    """Convertir les degrés en radian"""
    return valeur * math.pi / 180

def calcul_distance(lon_position, lat_position, lon_defib, lat_defib):
    """Calcul la distance entre 2 points grâce à leur coordonnées"""

    #Conversion des degrés en radian
    rad_lon_position = conversion_radian(lon_position)
    rad_lat_position = conversion_radian(lat_position)
    rad_lon_defib = conversion_radian(lon_defib)
    rad_lat_defib = conversion_radian(lat_defib)

    #Calcul de la distance, 6371 correspont au rayon de la terre en km
    x =(lon_defib - lon_position) * math.cos((lat_defib + lat_position) / 2)
    y = (lat_defib - lat_position)
    d = math.sqrt(x*x + y*y) * 6371

    return d

#Lecture des entrées
lon_position = float(input().replace(",","."))
lat_position = float(input().replace(",","."))
n = int(input())
distance_la_plus_courte = float("inf") # Initialisation de la distance minimale à l'infini
defib_le_plus_proche = "" #Initialisation du nom du debibrilateur le plus proche

#Parcourir la liste des défibrilateurs
for i in range(n):
    defib = input()
    infos_defib = defib.split(";")

    #Extraction des données du défibrilateur
    lon_defib = float(infos_defib[4].replace(",","."))
    lat_defib = float(infos_defib[5].replace(",","."))

    #Calcul de la distance entre l’utilisateur et le défibrilateur
    d = calcul_distance(lon_position, lat_position, lon_defib, lat_defib)

    #Si cette distance est la plus courte trouvé jusqu’à présent, mettre à jour
    #la distance_la_plus_courte et le nom du défibrilateur
    if d < distance_la_plus_courte:
        distance_la_plus_courte = d
        defib_le_plus_proche = infos_defib[1]

#Afficher le nom du défibrilateur le plus proche
print(defib_le_plus_proche)
