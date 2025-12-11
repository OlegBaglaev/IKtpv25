k=[]
s=[]

def registreemine(k:list,s:list)->any:
    kasutaja=input("Sisesta kasutaja nimi: ")
    if kasutaja in k:
       print("Selline kasutaja juba eksisteerib!")
       return None
    parool = input("Sisesta parool(Arvud!): ")
    k.append(kasutaja)
    s.append(parool)
    print("Kasutaja registreeritud!")
    return kasutaja


def autoriseerimine(k:list,s:list)->any:
    kasutaja=input("Siesta kasutaja nimi: ")
    if kasutaja in k:
        id = k.index(kasutaja)
        parool=input("Sisesta parool(Arvud!): ")
        if s[id] == parool:
            print("Kasutaja autoriseeritud!")
            return kasutaja
        else:
            print("Vigane parool!")
    else:
        ("Vigane kasutaja nimi!")


def  parooli_muutmine(k:list,s:list)->any:
    kasutaja=input("Siesta kasutaja nimi: ")
    if kasutaja in k:
        id = k.index(kasutaja)
        parool=input("Sisesta parool(Arvud!): ")
        if s[id] == parool:
            uus_parool=("Sisesta uus parool(Arvud!): ")
            s[id]=uus_parool
            print("Parool on muudetud!")
        else:
            print("Vale parool!")
    else:print("Sellist kasutajat ei ole.")
            
            

def parooli_taastamine(k:list,s:list)->any:
     kasutaja=input("Siesta kasutaja nimi: ")
     if kasutaja in k:
          id = k.index(kasutaja)
          parool=input

    
    


    