#Töö 5.1
#1
def float_kontroll(sisend:(str))->float:
    
    
    while True:
        try:
            arv=float(sisend)
            return arv
        except ValueError:
            sisend=input("Palun sisesta arv: ")
            
#2
def int_kontroll(sisend:str)->int:
    while True:
        try:
            arv=int(sisend)
            return arv
        except ValueError:
            sisent=input("Palun sisesta arv: ")


#3





#1
def arithmetic(a:float,b:float,tehe:str)->any:
    """Lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    Muul juhul tagastab "Tundmatu tehe"
    :param float a: esimene arv
    :param float b: teise arv
    :param str tehe: tehe, mis tuleb teha
    :return/rtype: tehte tulemus float või str
    """
    if tehe in ["+","-","*","/"]:
        if tehe=="/" and  b==0:
            vastus="Nulliga jagamine pole lubatud"
        else:
            vastus=eval(f"{a}{tehe}{b}")
    else:
        vastus="Tundmatu tehe"
    return vastus

#2
def is_year_leap(aasta:int)->bool:

    if aasta % 4 == 0 and aasta % 100 !=0:
        return True
    else:
        return False

#3
def square(külg:float)->any:
    ümbermõõt=4*külg
    pindala=külg ** 2
    diagonaal = külg * (2 ** 0.5)
    return ümbermõõt, pindala, diagonaal

#4
def season(kuu_number:int)->str:
    if kuu_number in [12,1,2]:
        return "Talv"
    elif kuu_number in [3,4,5]:
        return "Kevad"
    elif kuu_number in [6,7,8]:
        return "Suvi"
    elif kuu_number in [9,10,11]:
        return "Sügis"
    else:
        return"Vigane kuu number"

#5
def bank(a:float,years:int)->float:
    intress=0.1 
    for i in range(years):
        a+=a*intress
    return a