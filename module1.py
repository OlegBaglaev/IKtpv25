# päev =input("Sisesta päeva nimetus (näiteks esmaspäev): ")
# #1. Kui on neljapäev, siis Huraa, Programmeerimine!
# if päev.lower()=="neljapäev":
#     print("Huraa, Programmeerimine!")


# #2 Kui on neljapäev, siis Huraa, Programmeerimine! kui on reede siis"Igatsen, programmeerimine
# if päev.lower()=="neljapäev":
#     print("Huraa, programmeerimine:")
# else:
#     print("Igatsen, programmeerida tahaks!")


# #3 Tööpäevad ja nädalavahetus
# if päev.lower()=="laupäev" or päev.lower()=="pühapäev":
#     print("Lõpuks ometi nädalavahetus!")
# else:
#     print("Tööpäev, pean tööl käima!")

# #1-esmaspäev, 2-teisipäev, 3-kolmapäev, 4- neljapäev, 5-reede, 6-laupäev,7-pühapäev
# paev_number=int(input("Sisesta päeva number (1-7): "))
# if paev_number==1:
#     print("Esmaspäev")
# elif paev_number==2:
#     print("Teisipäev")
# elif paev_number==3:
#     print("Kolmapäev")
# elif paev_number==4:
#     print("Neljapäev")
# elif paev_number==5:
#     print("Reede")
# elif paev_number==6:
#     print("Laupäev")
# elif paev_number==7:
#     print("Pühapäev")
# else:
#     print("Välha number! Palun sisesta number vahemikus 1-7")




# #  1. Juku
# # a Kui eesnimi on Juku siis lähme Jukuga kinno. Aga teeme seda nii, kui nimi oli kirjutatud suurtähtedega.
# # b Lisa valiku, kus Juku vanuse alusel otsustate mis pilet talle vaja osta. (Tee kontroll, kas sisestatud arv on täisarv)
# # <6 aastad  - tasuta
# # 6-14 - lastepilet
# # 15-65 - täispilet
# # >65 - sooduspilet
# # <0 ja >100 viga andmetega
# eesnimi=input("Sisesta eesnimi: ")
# if eesnimi=="JUKU":
#     print("Lähme Jukuga kinno!")
#     vanus=input("Sisesta Juku vanus: ")
#     if vanus.isdigit():
#         vanus=int(vanus)
#         if vanus<0 or vanus>100:
#             print("Viga andmetega!")
#         elif vanus<6:
#             print("Pilet on tasuta!")
#         elif vanus<=14:
#             print("Lastepilet")
#         elif vanus<=65:
#             print("Täispilet")
#         else:
#             print("Sooduspilet")
#     else:
#         print("Palun sisesta vanus täisarvuna!")

# # 2 Pinginaabrid
# # Küsi kahe inimese nimed. 
# # Kui nimed koosnevad ainult tähedest siis  teavita kasutajat, 
# # kas nad on täna pinginaabrid või ei mitte.
# nimi1 = input("Sisesta nimi").capitalize()
# nimi2 = input("Sisesta nimi").capitalize()
# if nimi1.isalpha() and nimi2.isaplha():
#     if nimi1=="Oleg" and nimi2=="Danil" or nimi1=="Danil" and nimi2=="Oleg":
#         print(f"{nimi1} ja {nimi2} on täna pinginaabrid")
#     else:
#         print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid")
# else:
#     print("Palun sisesta ainult tähed")

# 3 Remont
# Küsi ristkülikukujulise toa seinte pikkused ning arvuta põranda pindala. Küsi kasutajalt remondi tegemise soov, kui ta on positiivne, siis küsi kui palju maksab ruutmeeter ja leia põranda vahetamise hind
# Lisaküsimus: kas ta teeb remonti ise või teeb seda professionaali abiga? Kui tegemist on professionaaliga, siis palun arvutage välja, kui palju remont koos tööga maksab.

# pikkus = int(input("Sisestage pikkus: "))
# laius = int(input("Sisestage laius: "))
# if pikkus>0 and laius>0:

#     pindala = pikkus * laius
#     print(f"pindala suurus on {pindala}")
#     user = input("Kas soovite remondi teha? ").capitalize()
#     if user.isalpha() and user == "Jah":
#         hind =float(input("Ruutmeetri hind? "))
#         if hind > 0:
#             remondi_hind = hind * pindala
#             print(f"Remondi summa on {remondi_hind}")
#             kes = input("Kes teeb remondi(ise või töötaja)?").capitalize()
#             if kes.isalpha() and kes == "ise":
#                 print(f"Siis summa on {remondi_hind}")
#             else:
#                 print(f"Siis summa on {remondi_hind + 300}")
#         else:
#             print("Hind ei saa olla negatiivne")
#     else:
#         print("Head aega!")
# else:
#     print("Arvud peavad olema suurem kui 0")


# 4 Allahindus
#  Leia 30% soodustusega hinna, kui alghind on suurem kui 700

# hind = input("Hind: ")
# if hind.isdigit():
#     hind = float(hind)
#     if hind > 700:
#         hind *= 0.7
#         print(f"Soodus hind võrdub {hind}")
# else:
#     print("On vaja numbri sisestada")

# 5 Temperatuur
# Küsi temperatuur ning teata, kas see on üle 18 kraadi (soovitav toasoojus talvel)
# try:
#     temperatuur = float(input("Sisesta temperatuur: "))
#     if temperatuur > 18:
#         print("Soovitavtav toasoojus talvel")
#     else:
#         print("Võib olla jahe")
# except:
#     print("Palun sisesta temperatuur ujukommarvuna")

# 6 Pikkus
# Küsi inimese pikkus ning teata, kas ta on lühike, keskmine või pikk (piirid pane ise paika)

# p = float(input("Sisesta oma pikkus (Sentimeetrid): "))
# if p < 160:
#     print("Sa oled lühike")
# elif p > 160 and p < 180:
#     print("Sa oled keskmise pikkusega")
# elif p > 180:
#     print("Sa oled pikk")
# else:
#     print("Proovi uuesti")

# 7 Pikkus ja sugu
# Küsi inimeselt pikkus ja sugu ning teata, kas ta on lühike, keskmine või pikk (mitu tingimusplokki võib olla üksteise sees).
# sugu = input("Mis soost sa oled? ").capitalize()
# p = float(input("Sisesta oma pikkus (Sentimeetrites): "))

# if sugu == "Mees":
#     print("Sa oled mees")
# elif sugu == "Naine":
#     print("Sa oled naine")
# else:
#     print("Proovi uuesti")

# if p < 160:
#     print("Sa oled lühike")
# elif 160 <= p <= 180:
#     print("Sa oled keskmise pikkusega")
# elif p > 180:
#     print("Sa oled pikk")
# else:
#     print("Proovi uuesti")

# 8 Poes
# Küsi inimeselt poes eraldi kas ta soovib osta piima, saia, leiba jne. 
# Loo juhuslikud hinnad ja küsi mitu tükki tahad osta, kui tahad. Teata, mis summa maksma läheb(Kuva ekraanil tšekk).

import random
hind1 = hind2 = hind3 = 0
sai = input("Kas te soovite osta sai? ").capitalize()
if sai=="Jah":
    mitu = int(input("Mitu saiad te soovite osta?: "))
    hind1 = round(mitu * random.uniform(0.6, 2.0),2)
else:
    print("Ei soovi saia")
piim = input("Kas te soovite osta piima? ").capitalize()
if piim=="Jah":
    mitu2 = int(input("Mitu Piima te soovite osta: "))
    hind2 = round(mitu2 * random.uniform(1.0, 2.5),2)
else:
    print("Ei soovi piima")
leib = input("Kas te soovite osta leib? ").capitalize()
if leib=="Jah":
    mitu3 = int(input("Mitu leiba te soovite osta?: "))
    hind3 = round(mitu3 * random.uniform(0.5, 1.5),2)
else:
    print("Ei soovi leiba")

print("Teie tšekk:")
print(f"Saiad: {hind1} EUR")
print(f"Piim: {hind2} EUR")
print(f"Leib: {hind3} EUR")
kokku = hind1 + hind2 + hind3
print(f"Kokku: {kokku} EUR")

