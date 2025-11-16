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
                print("   /V\    ")
                print("  / V \   ")
                print(" / V V \  ")
                print("/VV V VV\ ")
            break
        else:
            print("Arv peab olema vahemikus 1 kuni 9!")
    except ValueError:
          print("Palun sisesta täisarv!")

#Korruta kõik paaritud väärtused vahemikus 0 kuni kasutaja sisestatud arvuni (R).

R = int(input("Sisesta täisarv: "))
kor = 1
for i in range(0, R + 1):
    if i % 2 == 0:
        kor *= i

print("Paarisarvude korrutis 0-st kuni", R, "võrdub", korrutis)

#Antud on N arvu (N on juhuslik). Leia, mitu positiivset arvu nende seas on.       

