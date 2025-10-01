
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
nimi=input("Sisesta oma nimi").capitalize()#sisend ja ootab enterit
print(f"Tere maailm! Tervitan sind {nimi}")
vanus=int(input("Sisesta oma vanus: "))#int teisendab stringi täisarvuks
print(f"Tere maailm! Tervitan sind {nimi.upper()}, Sa oled {vanus} aastat vana")#upper muudab suurtähed
print(f"Tere maailm! Tervitan sind {nimi.lower()}, Sa oled {vanus} aastat vana")#lower muudab väiketähed