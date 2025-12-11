from My_module import *
while True:
    print("KasutajaRegistreerimine ja Autoriseerimine Süsteem")
    print("Valige soovitud funktsioon")
    print("1️ - Registreerimine")
    print("2 - Autoriseerimine")
    print("3 - Nime või parooli muutmine")
    print("4 - Unustatud parooli taastamine")
    print("5️ - Lõpetamine Väljumine")
    valik=input("Sisesta valik: ")
    while True:
        if valik=="1":
            registreemine(k,s)
            break
        elif valik=="2":
            autoriseerimine(k,s)
            break
        elif valik=="3":
            parooli_muutmine
            break
        elif valik=="4":
            parooli_taastamine
            break
        elif valik=="5":
            break
        else:
            print("Vigane valik, proovi uuesti")