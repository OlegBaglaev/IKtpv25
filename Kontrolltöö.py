#1. variant
#Kirjuta programm, mis antud arvu n (vahemikus 1 kuni 9) põhjal kuvab ekraanile n kuuske.
#Ühe kuuse suurus on 4×9 märki, kahe kuuse vahel peab olema üks tühikurida (tühikust koosnev veerg).
#Lubatud on lisada ka tühikurida pärast viimast kuuske.
#Et joonistamine oleks lihtsam, kopeeri kuusekuju näitest arenduskeskkonda.
#Kuused peavad asetsema horisontaalselt.

while True:
    try:
        N = int(input("Sisesta täisarv (1–9): "))
        
        if 1 <= N <= 9:
            for i in range(N):
                print("   /V\\    ")
                print("  / V \\   ")
                print(" / V V \\  ")
                print("/VV V VV\\ ")
            break
        else:
            print("Arv peab olema vahemikus 1 kuni 9!")

    except ValueError:
        print("Palun sisesta täisarv!")


#Korruta kõik paaritud väärtused vahemikus 0 kuni kasutaja sisestatud arvuni (R).

while True:
    try:
        R = int(input("Sisesta täisarv: "))  
        break  
    except ValueError:
        print("Viga: palun sisesta täisarv!")
kor = 1
for i in range(0, R + 1):
    if i % 2 == 0:
        kor *= i

print("Paarisarvude korrutis 0-st kuni", R, "võrdub", korrutis)

#Antud on N arvu (N on juhuslik). Leia, mitu positiivset arvu nende seas on.       

N = input("Sisesta arvud: ").split()
pos = 0  
for num in (N):
    if float(num) > 0:  
        pos += 1

print("Positiivne arvud on:", pos)

#Loenda paaris- ja paaritud numbrid sisestatud naturaalarvus.
#Näide: arv 34560 → 3 paarisarvu (4, 6 ja 0) ja 2 paaritut (3 ja 5).

num = input("Sisesta naturaalarv: ").strip()
paaris_arv = 0
paaritu_arv = 0
for digit in num:
    if digit.isdigit():  
        if int(digit) % 2 == 0:
            paaris_arv += 1
        else:
            paaritu_arv += 1

print(f"Paaris arv: {paaris_arv}")
print(f"Paaritu: {paaritu_arv}")

#Leia arvude A kuni B summa ja kuva tulemus ekraanile.

A = int(input("Sisesta number A: "))
B = int(input("Sisesta number B: "))

summa = 0

for i in range(A, B + 1):  
    summa += i             

print("Arvude summa A-st kuni B-ni on:", summa)
