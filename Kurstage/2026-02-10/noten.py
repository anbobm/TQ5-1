punktzahl = int(input("Gib Punktzahl SOFORT: "))

if punktzahl >= 92:
    print("sehr gut")
elif punktzahl >= 81:
    print("gut")
elif punktzahl >= 67:
    print("befriedigend")
elif punktzahl >= 50:
    print("ausreichend")
elif punktzahl >= 30:
    print("mangelhaft")
else:
    print("ungenügend")