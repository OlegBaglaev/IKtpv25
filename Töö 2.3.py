#1 samm
# print("Tere! Olen sinu uus sõber - Python!")
# nimi = input("Mis on sinu nimi?: ")
# print(nimi, "oi kui ilus nimi!")
# try:
#     küsimus = int(input(f"{nimi}, kas leian Sinu keha indeksi? (0 - ei, 1 - jah): "))
#     if küsimus == 1:
#         print("indeksi leidmine käib nüüd!")
    
#     elif küsimus == 0:
#          print("Okei, võib-olla järgmine kord!")
#     else:
#         print("Palun sisesta 0 või 1!")
# except:
#     print("Palun sisesta kehtiv number (0 või 1)!")

#2 samm

# print("Tere! Olen sinu uus sõber - Python!")
# nimi = input("Mis on sinu nimi?: ")
# print(nimi, "oi kui ilus nimi!")
# try:
#     küsimus = int(input(f"{nimi}, kas leian Sinu keha indeksi? (0 - ei, 1 - jah): "))
#     if küsimus == 1:
#         print("indeksi leidmine käib nüüd!")
#         pikkus = float(input("Sisesta oma pikkus sentimeetrites "))
#         mass   = float(input("Sisesta oma mass kilogrammides "))
#         KMI    = mass / (0.01 * pikkus) ** 2
#         print(f"{nimi}! Sinu kehamassiindeks on {round(KMI, 1)}")
#     elif küsimus == 0:
#          print("Okei, võib-olla järgmine kord!")
#     else:
#         print("Palun sisesta 0 või 1!")
# except:
#     print("Palun sisesta kehtiv number (0 või 1)!")

#3 samm

# print("Tere! Olen sinu uus sõber - Python!")
# nimi = input("Mis on sinu nimi?: ")
# print(nimi, "oi kui ilus nimi!")
# try:
#     küsimus = int(input(f"{nimi}, kas leian Sinu keha indeksi? (0 - ei, 1 - jah): "))
#     if küsimus == 1:
#         print("indeksi leidmine käib nüüd!")
#         while True:
#             try:
#                  pikkus = int(input("Sisesta oma pikkus sentimeetrites "))
#                  if pikkus <= 250:
#                      break
#                  else:
#                      print("Pikkus peab olema vahemikus 0 kuni 250 cm. Proovi uuesti.")
#             except:
#                 print("Vale pikkuse formaat. Palun sisesta täisarv.")
#         while True:
#             try:
#                  mass = int(input("Sisesta oma mass kilogrammides "))
#                  if 0 < mass < 300:
#                      break
#                  else:
#                      print("Mass peab olema vahemikus 0 kuni 300 kg. Proovi uuesti.")
#             except:
#                 print("Vale massi formaat. Palun sisesta arv.")
# except:

# #4 samm        

# print("Tere! Olen sinu uus sõber - Python!")
# nimi = input("Mis on sinu nimi?: ")
# print(nimi, "oi kui ilus nimi!")
# try:
#     küsimus = int(input(f"{nimi}, kas leian Sinu keha indeksi? (0 - ei, 1 - jah): "))
#     if küsimus == 1:
#         print("indeksi leidmine käib nüüd!")
#         while True:
#             try:
#                  pikkus = int(input("Sisesta oma pikkus sentimeetrites "))
#                  if pikkus <= 250:
#                      break
#                  else:
#                      print("Pikkus peab olema vahemikus 0 kuni 250 cm. Proovi uuesti.")
#             except:
#                 print("Vale pikkuse formaat. Palun sisesta täisarv.")
#         while True:
#             try:
#                  mass = int(input("Sisesta oma mass kilogrammides "))
#                  if 0 < mass < 300:
#                      break
#                  else:
#                      print("Mass peab olema vahemikus 0 kuni 300 kg. Proovi uuesti.")
#             except:
#                 print("Vale massi formaat. Palun sisesta arv.")
#         indeks = round(mass / (0.01 * pikkus) ** 2, 2)
#         print(f"{nimi}! Sinu kehamassiindeks on {indeks}")
#         if indeks < 16:
#             print("Tervisele ohtlik alakaal")
#         elif indeks > 16 and indeks < 19:
#             print("Alakaal")
#         elif indeks > 20 and indeks < 25:
#             print("Normaalkaal")
#         elif indeks > 26 and indeks < 30:
#             print("Ülekaal")
#         elif indeks > 31 and indeks < 35:
#             print("Rasvumine")
#         elif indeks > 36 and indeks < 40:
#             print("Tõsine rasvumine")
#         elif indeks > 40:
#             print("Haiglaslik rasvumine")
#     elif küsimus == 0:
#             print("Kahju! See on väga kasulik info!")
#     else:
#         print("Palun sisesta 0 või 1!")
# except:
#     print("Palun sisesta kehtiv number (0 või 1)!")
# print(f"Kohtumiseni {nimi} Igavesti Sinu, Python!")
     
        
        
        
        
        
        
        
        
        
        
        
        
     