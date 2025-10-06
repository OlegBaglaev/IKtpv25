# Harjutus 1.1. Muutajad ja sisend
# 6
# Leidke järgnevast näiteprogrammist loogiline viga:
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = aeg / teepikkus
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg 
print("Sinu kiirus oli " + str(kiirus) + " km/h")

# 5.
# Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
import math 
N=float(input("Sisesta maatüki pikkus N (meeter): "))
M=float(input("Sisesta maatüki pikkus M (meeter): "))
diagonaal = math.sqrt(N**2 + M**2)
print(f"Maatüki diagonaal on {diagonaal:.2f} meetrit.")

# 4
# Puu läbimõõdu arvutamine
# Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.
import math
umbermõõt =float(input("Sisesta puu ümbermõõt"))
labimõõt = umbermõõt / math.pi
print(f"Puu läbimõõt on {labimõõt:.2f}")




# 3
# Kirjuta enda koodis laual olevate kommide arv muutujasse(kommide arv on juhuslik). 
# Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
# Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. 
# Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on.
import random
kommide_arv = random.randint(10, 50)
print("Laual on", kommide_arv, "kommi.")
võetavad_kommid = int(input("Mitu kommi soovid laualt võtta? "))
kommide_arv -= võetavad_kommid
print("Nüüd on laual", kommide_arv, "kommi.")


# 2
# Mis tüüpi on järgnevad muutujad:
# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 1.65
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# Kirjuta kood tüüpide kontrollimiseks.
vanus = 18              #int
eesnimi = "Jaak"        #str
pikkus = 1.65           #float
Kas_käib_koolis = True  #bool
print(f"vanus {vanus} on: {type(vanus)}")
print(f"eesnimi {eesnimi} on: {type(eesnimi)}")
print(f"pikkus {pikkus} on: {type(pikkus)}")
print(f"Kas_käib_koolis {Kas_käib_koolis} on: {type(Kas_käib_koolis)}")

# Harjutus 1.1. Muutajad ja sisend
# 1.
# Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# “Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”
print("Tere maailm!")

