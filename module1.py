päev =input("Sisesta päeva nimetus (näiteks esmaspäev): ")
#1. Kui on neljapäev, siis Huraa, Programmeerimine!
if päev.lower()=="neljapäev":
    print("Huraa, Programmeerimine!")


#2 Kui on neljapäev, siis Huraa, Programmeerimine! kui on reede siis"Igatsen, programmeerimine
if päev.lower()=="neljapäev":
    print("Huraa, programmeerimine:")
else:
    print("Igatsen, programmeerida tahaks!")


#3 Tööpäevad ja nädalavahetus
if päev.lower()=="laupäev" or päev.lower()=="pühapäev":
    print("Lõpuks ometi nädalavahetus!")
else:
    print("Tööpäev, pean tööl käima!")

