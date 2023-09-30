#Tugas perulangan While dan For
# Zhoif Fachdiat dengan NIM 2309106014 dari kelas A23

print("Output 1 :")
i = 1
while i <= 10:
    print(i)
    i += 1

print("\nOutput 2 :")
i = 1
while i <= 10:
    print(i, end=' ')
    i += 1

print("\n\nOutput 3 :")
i = 10
while i >= 1:
    print(i, end=' ')
    i -= 1

print("\n\nOutput 4 :")
i = 1
while i <= 10:
    print(i * 2, end=' ')
    i += 1

print("\n\nOutput 4a :")
for _ in range(5):
    for i in range(1, 6):
        print(i, end=' ')
    print()

print("\nOutput 4b :")
for _ in range(5):
    for i in range(1, 6):
        if i == 3:
            print(0, end=' ')
        else:
            print(i, end=' ')
    print()

print("\nOutput 4c :")
for baris in range(5):
    for kolom in range(1, 6):
        if kolom == 2:
            print(2, end=' ')
        elif kolom == 4:
            print(4, end=' ')
        else:
            print(0, end=' ')
    print()

print("\nOutput 4d :")
for baris in range(3):
    for kolom in range(1, 6):
        print(kolom, end=' ')
    print()
    if baris==2:
        break
    for _ in range(5):
        print(0, end=' ')
    print()

print("\nOutput 4e :")
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print('a', end=' ')
        else:
            print(j, end=' ')
    print()

print("\nOutput 4f :")
tot = 1
for i in range(1, 6):
    for j in range(5):
        print(tot, end=' ')
        tot += 1
    print()

ganjil = sum(1 for i in range(1, 26) if i % 2 != 0)
genap = 25 - ganjil
print(f"\nAda {ganjil} angka bilangan ganjil")
print(f"Ada {genap} angka bilangan genap")

print("\nOutput 5 :")
for i in range(1, 6):
    for j in range(i):
        print(i, end=' ')
    print()

print("\nOutput 6 :")
for i in range(1, 6):
    for j in range(i):
        print(4, end=' ')
    print()

print("\nOutput 7 :")
