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