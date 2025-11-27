#6️ Arvud

#Leia loendi suurim arv, jaga see loendi pikkusega ja asenda see tulemusena.
from random import *
loend_arvud=[]
mitu=randint(2,20)
for i in range(mitu):
    elem=randint(0,100)
    loend_arvud.append(elem)
print(f"Alguses loend: loend_arvud")
suurim=max(loend_arvud)
kus_asub=loend_arvud.index(suurim)
suurim_muudatud=suurim/mitu
loend_arvud[kus_asub]=round(suurim_muudatud,2)
print(f"Muutmise järel:  {loend_arvud}")



# 5️ Vahetus 
# from random import *
# Vaheta loendis esimene ja viimane element, teine ja eelviimane jne.
# Küsi kasutajalt, mitu paari vahetada. loendis on min 2 elem.
# l_arvud=[]
# l_tähed=[]
# l_kaashäälikud=[]
# mitu=randint(2,20)

# for i in range(mitu):
#     elem=randint(0,100)
#     l_arvud.append(elem)
#     elem=chr(randint(65,90))
#     l_tähed.append(elem)
#     elem=choice(k)
#     l_kaashäälikud.append(elem)
# print(f"kokku on {mitu} elemente loendis")

# while True:
#     try:
#         paaride_arv=int(input(f"Sisesta mitu paari soovid vahetada: "))
#         if 1<= paaride_arv<=mitu//2:
#             break
#         else:
#             print(f"Arv peab olema vahemikus 1 kuni {mitu//2}")
#     except:
#         print("Vigane andmetüüom, pproovi uuesti")




# 4️ Postiindeks 

# Eestis koosnevad postiindeksid 5 numbrist, millest esimene number tähistab maakonda:
# 1 – Tallinn 
# 2 – Narva, Narva-Jõesuu 
# 3 – Kohtla-Järve 
# 4 – Ida-Virumaa, Lääne-Virumaa, Jõgevamaa 
# 5 – Tartu linn 
# 6 – Tartumaa, Põlvamaa, Võrumaa, Valgamaa 
# 7 – Viljandimaa, Järvamaa, Harjumaa, Raplamaa 
# 8 – Pärnumaa 
# 9 – Läänemaa, Hiiumaa, Saaremaa
# Kontrolli kasutaja sisestatud postiindeksit.
# Näita, millisesse maakonda see kuulub.
# Erireegel:
#     Tallinn, Narva, Kohtla-Järve → „Mine merre!”
#     Teised → „Mine metsa!”

indexid=["Tallinn","Narva,Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa,Jõgevamaa","Tartu linn ","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
while True:
    try:
        index=int(input("Sisesta oma postiindeks (5-kohaline arv): "))
        if 10000<=index<=99999:
            break
        else:
            print("Postiindeks peab olema 5-kohaline arv")
    except:
        print("vigane andmetüüp")
index_list=list(index)
n1=int(index_list[0])
print(f"Sinu postiindeksiga {index} kuulud piirkonda: {indexid[n1-1]}")
if n1 in [0,1,2,7]:
    print("Mine merre!")
else:
    print("Mine metsa!")












# 3️ Tärnide lintdiagramm ⭐

# Kasuta loendis olevaid arve ja joonista tärnidega diagramm.
# ******************
# *******************
# ********************************
# *****************************************
# ****************************************************
# ************

arvud=[2,5,6,10,8,9,12]

      


   


# 2️ Loendid
# 2.3 Vanused 

# Koosta vanuste loend ja leia:
#     suurim
#     väikseim
#     kogusumma
#     keskmine

v=[5,10,15,16,22,24,12,35,21]
suurim=max(v)
väiksem=min(v)
kogusumma=sum(v)
keskmine=sum(v) / len(v)
print(suurim)
print(väiksem)
print(kogusumma)
print(keskmine)




# 2.2 Kordustega nimed 

# Antud on loend kordustega.
# Koosta programm, mis väljastab nimed ilma kordusteta.

nimed =["Juku","Mari","Peeter","Juku","Jüri","Mari","Jüri"]
i_korduseta=list(set(nimed))    
print(i_korduseta)








# 2.1 Nimed 

#     Küsi kasutajalt viis nime.
#     Salvesta nimed loendisse ja kuva need tähestikulises järjekorras.
#     Kuva viimane lisatud nimi.
#     Lisa võimalus nimekirjas olevaid nimesid muuta

nimed=[]
for i in range(5):
    nimi= input("Sisesta nimi ")
    nimed.append(nimi)
    
print(nimed)
viimane_nimi = nimed[-1]
nimed.sort()
print(nimed)
print(viimane_nimi)

replace =input("Kas te soovite muuta nimi? ").lower
if replace =="jah":
    v_n=input("Mis nimi muutame?: ")
    u_n=input("Mis uus nimi? ")
    find = nimed.index(v_n)
    nimed[find]=u_n
    print(nimed)
else:
    print(nimed)








#1️ Sõna või lause analüüs
#Sisesta sõna või lause.
#Loenda:

#    mitu täishäälikut 
#    mitu kaashäälikut 
#    kui sisestati lause – loenda ka tühikud ja kirjavahemärgid 

import string
t=["a","e","i","o","u","ü","ä","ö","õ"]
k=["b","c","d","f","g","h","j","k","l","m","n"]
m=string.punctuation + string.whitespace
sõna_lause=input("Sisesta sõna või lause: ").lower()
täishäälikud=0
kaashäälikud=0
märgid=0
for täht in sõna_lause:
    if täht in t:
        täishäälikud+=1
    elif täht in k:
        kaashäälikud+=1
    elif täht in m:
        märgid+=1
print(f"Sõnas/lauses on {täishäälikud} täishäälikud {kaashäälikud} kaashäälikut ja {märgid} märgid ")







#List
#loome listi
l=[] #tühi list
print(f"Listi algseis: {l}")
while True:
    print("Tee valik:")
    print("1 - Lisa elemente\n2 - lisa elemente pos-le \n3 - Eemalda elemente pos järgi \n4 - Eemalda element nimi järgi \n5 - sorteeri listi \n6 - tühjenda listˇ\n7 - teise list ")
    while True:
        try:
            valik=int(input())
            break
        except:
              print("Arvud: 1...n")
    print("Töö listiga")
    
    if valik==1:
        while True:
            try:
                i=int(input("Mitu elementi soovid lisada?: "))
                if i>0:
                    break
                else:
                    print("Arvud´on vaja > 0")
            except:
                print("Täisarvud on vaja kasutada")
        for element_id in range(i):
            element=input(f"{element_id}. element: ")
            l.append(element)
        print(f"Uuendatud list on {l}")

    elif valik==2:
        while True:
            try:
                pos=int(input(f"Positsioon kuhu soovid lisada(0-{len(l)}): "))
                if 0<=pos<=len(l):
                    break
                else:
                    print(f"Positsioon peab olema 0 kuni {len(l)}")
            except:
                print("Positsioon on vaja kasutada")
        element=input("Sisesta element mida soovid lisada: ")
        l.insert(pos,element) #lisab elemendi soovitud positsioonile
        
    elif valik==3:
        while True:
            try:
                pos=int(input(f"Positsioon kuhu soovid eemalda(0-{len(l)-1}): "))
                if 0<=pos<=len(l)-1:
                    break
                else:
                    print(f"Positsioon peab olema vahemikus 0 kuni {len(l)-1}")
            except: 
                print("Positsioon on vaja kasutada")
        eem_element=l.pop(pos) #eemaldab elemendi soovituud positsioonilt
        print(f"Eemaldatud element on {eem_element}")
    
    elif valik==4:
        element=input("Sisesta element mida soovid eemaldada: ")
        mitu=l.count(element)
        if mitu==0:
                print("Elementi ei leitud")
        else:
            for e in range(mitu):
                print(f"Eemaldame element'{element}' {l.index(element)} positsioonilt")
                l.remove(element) #eemaldab esileidu elemendi
        print(f"Eemaldati {mitu} elementi ")

    elif valik==5:
        print("Vali sorteerimise suund:")
        print("1 – kasvavalt ")
        print("2 – kahanevalt ")
        s=int(input("Valik: "))
        if s==1:
            l.sort()
            print("List sorteeriti kasvavalt.")
        else:
            l.sort(reverse=True)
            print("List sorteeriti kahanevalt.")
            print(f"Uuendatud list: {l}")
    
    elif valik==6:
        l.clear()
        print("List on tühjendud")

    elif valik == 7:
        print("Lisa teise loendi elemendid praegusesse loendisse.")
        l2 = []  
        kogus = int(input("Mitu elementi soovid lisada teise loendisse? "))
        for i in range(kogus):
            el = input(f"Sisesta element {i+1}: ")
            l2.append(el)

    l.extend(l2)
    print(f"Listi laiendati. Uuendatud list: {l}")
            
    print(f"Uuendatud list on {l}")    


