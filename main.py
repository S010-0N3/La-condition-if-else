### creer une boucle qui separe les mots via leurs tailles :

planete_names = ["Mercure","Terre","Venus","Mars","Jupiter","Saturne","Neptune","Uranus"]

long_names =[]
short_names = []
### len sert a compter les elements ,la (u) etant chaque planete, il compte chaque lettre
for u in planete_names:
  if len(u) > 5:
    long_names.append(u)
  else:
    short_names.append(u)

print(long_names)
print(short_names)


### Compter les éléments d'une liste et présenter les résultats dans un dictionnaire.

fruits = ["Citron","Banane","Pomme","Pomme","Pomme","Banane","Banane","Pomme"]

#liste vide
fruits_count = {}

#boucle pour verifier et ajoute +1 a fruit count, si on regarde c'est l'ajout d'un element de dictionnaire:
for item in fruits:
  if item in fruits_count:
    fruits_count[item] = fruits_count[item] + 1
  else:
    fruits_count[item] = 1
print(fruits_count)

#RAPPEL : ajout element dand une liste
op = {}
op["tarte"]= 5
print(op)

