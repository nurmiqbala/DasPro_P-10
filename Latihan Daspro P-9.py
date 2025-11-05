#Nur Muhammad Iqbal Alfajri
#2502342
#1A

#Soal 1
def fib(A):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(0, A-2):
        c = a + b
        a = b
        b = c
        print(b)
fib(10)
fib(20)

#Soal 2
def VolumeTabung(r, t):
    V = 22/7 * r * r * t
    return V

print(VolumeTabung(7, 10))
print(VolumeTabung(14,10))

#Soal 3
def NilaiTotal(*angka):
    A = sum(angka)
    B = len(angka)
    C = A / B
    print(f"Angka = {angka}")
    print("Total = ", A)
    print("Rata-rata = ", C)

NilaiTotal(2,3,5,10)
NilaiTotal(1,2,3,4,5,6,7,8,9,10)
    