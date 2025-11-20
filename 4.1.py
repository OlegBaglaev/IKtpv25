#replace()
# import msvcrt
# täht=""
# while True:
#     t=msvcrt.getwch()
#     print(t.replcace(t,"*"),end="",flush=True)
#     täht+=t
#     if t== '\r':
#         break
# print()
# print(täht)





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
    


