nota= int(input("Entra la teva nota: "))
if nota < 5 and nota > 0:
    print("Suspès")
elif nota >= 5 and nota < 6:
    print("Sufi")
elif nota >= 6 and nota < 7:
    print("Bé")
elif nota >= 7 and nota < 9:
    print("Notable")
elif nota >= 9 and nota < 10.1:
    print("Exel·lent")

else:
    print("La nota és sobre deu màquina")

