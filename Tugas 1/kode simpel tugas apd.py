nilai = int(input("Input angka dari 0-100 = "))
try:
    grades = {
        (90, 100): "A+",
        (80, 90): "A-",
        (75, 80): "B+",
        (70, 75): "B-",
        (65, 70): "C+",
        (60, 65): "C-",
        (50, 60): "D",
        (0, 50): "E"
    }

    found = False

    for (lower, upper), grade in grades.items():
        if lower <= nilai <= upper:
            print(grade)
            found = True
            break

    if not found:
        print("Inputan tidak sesuai ketentuan")

except ValueError: