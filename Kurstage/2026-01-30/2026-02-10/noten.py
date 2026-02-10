punkt = int(input("Geben Sie Ihre Punktzahl (0-100) ein: "))
if punkt >= 92:
    print("sehr gut")
elif punkt >= 81:
    print("gut")
elif punkt >= 67:
    print("befriedigend")
elif punkt >= 50:
    print("ausreichend")
elif punkt >= 30:
    print("mangelhaft")
else:
    print("ungenügend")