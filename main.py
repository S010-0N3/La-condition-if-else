### creer une boucle qui separe les mots via leurs tailles :

planete_names = ["Mercure","Terre","Venus","Mars","Jupiter","Saturne","Neptune","Uranus"]

long_names =[]
short_names = []

for u in planete_names:
  if len(u) > 5:
    long_names.append(u)
  else:
    short_names.append(u)

print(long_names)
print(short_names)


### Compter les éléments d'une liste et présenter les résultats dans un dictionnaire.

fruits = ["Citron","Banane","Pomme","Pomme","Pomme","Banane","Banane","Pomme"]

fruits_count = {}

for item in fruits:
  if item in fruits_count:
    fruits_count[item] = fruits_count[item] + 1
  else:
    fruits_count[item] = 1

print(fruits_count)