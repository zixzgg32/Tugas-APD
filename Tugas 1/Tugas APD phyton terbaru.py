while True:
    try:
        nilai = int(input("Masukkan nilai anda = "))
        if 0 <= nilai <= 100:
            break
        else:
            print("Inputan yang benar adalah 0-100")
    except ValueError:
        print("Inputan anda salah, masukkan kembali nilai anda.")

if 90 <= nilai <= 100:
    print("A+")
elif 80 <= nilai < 90:
    print("A-")
elif 75 <= nilai < 80:
    print("B+")
elif 70 <= nilai < 75:
    print("B-")
elif 65 <= nilai < 70:
    print("C+")
elif 60 <= nilai < 65:
    print("C-")
elif 50 <= nilai < 60:
    print("D")
else:
    print("E")