# 1 Sisestatakse 15 arvu.
# Määrata, mitu neist on täisarvud.
# k=0 #loendur
# for i in range(15):
#     while True:
#         try:
#             arv=float(input(f"Sisesta {i+1}, arv: "))
#             break
#         except:
#             print("Vale andmetüüp")
              
#     if int(arv)==arv:
#           print(f"{arv} on täisarv")
#           k+=1
# print(f"Täisarve oli kokku {k} tk")

# # 2 Küsi kasutajalt arv A ja leia kõigi naturaalarvude summa vahemikus 1 kuni A.
# s=0 #summa
# while True:
#     try:
#         A=int(input("Sisesta A: "))
#         break
#     except:
#         print("Vale andmetüüp")
# for i in range(1,A+1):
#     s=s+i
# print(f"Summa vahemikus i kuni {A} võrdub{s}")

# 3 Sisestatakse 8 arvu.
# Leida nende korrutis (ainult positiivsete arvude puhul).
# k=1 #korrutis
# for i in range(8):
#     while True:
#         try:
#             arv=float(input(f"Sisesta {i+1}, arv: "))
#             if arv>0: break
#         except:
#             print("Vale andmetüüp")
#     k=k*arv
#     print(f"Korrutis võrdub {k}")
# print(f"Kõigi positiivsete arvude korrutis võrdub {k}")

# 4 Koosta programm, mis väljastab ekraanile arvude ruudud vahemikus 10 kuni 20.
# for i in range(10,20):
#     arv=i**2
#     print(f"Arvu {i} ruut on {arv}")

# 5 Koosta programm, mis arvutab ainult negatiivsete arvude summa N sisestatud arvu seast.
# N väärtus sisestatakse klaviatuurilt.

# N=int(input("Sisesta N: "))
# s=0
# for I in range(N):
#     arv = float(input("Sisesta arv: "))
#     if arv < 0: 
#         s += arv
# print("Negatiivne arvu summa on:", s)

# 6 Klaviatuurilt sisestatakse N arvu.
# Koosta programm, mis määrab sisestatud arvude seast:
N_arv=0
P_arv=0
Null_arv=0
N=int(input("Sisesta N:"))
for i in range(N):
           arv = float(input("Sisesta arv:"))
           if arv<0:
                N_Arv=N_arv+1 
           elif arv>0:
                P_arv=P_arv+1 
           elif arv==0:
                Null_arv=Null_arv+1 
           else:
               print("Sisesta arvud!")
print(f"Negatiivsete arvude arv on:{N_arv}")
print(f"Positiivsete arvude arv on:{P_arv}")
print(f"Nullide arv on:{Null_arv}")

