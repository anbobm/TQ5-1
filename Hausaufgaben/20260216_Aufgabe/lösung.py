liste = [11, 59, 5, 30, 91, 70, 8, 92, 47, 71, 43, 38, 29, 92, 72, 'melone', 45, 87, 66, 61, 51, 37, 45, 71, 26, 54, 5, 35, 71, 
         'birne', 42, 11, 26, 33, 53, 58, 87, 'apfel', 99, 95, 10, 59, 23, 64, 16, 8, 27, 34, 11, 2, 67, 46, 3, 65, 18, 80, 
         'melone', 49, 12, 25, 24, 9, 25, 74, 53, 50, 51, 17, 82, 69, 42, 41, 71, 93, 'birne', 
         6, 36, 73, 76, 38, 17, 34, 81, 89, 14, 72, 20, 61, 11, 22, 46, 75, 40, 22, 25, 80, 59, 62, 19, 93]

ziel = ['melone', 'birne', 'apfel']

index = liste[0]

print("Erste element: ", index)

for iter in range(len(liste)):
    element = liste[index]
    print(f"{element} mit index {index}")
    if element in ziel:
        print(f"Das Ziel erreicht: {element} an Position {index}")
        break

    index = element

