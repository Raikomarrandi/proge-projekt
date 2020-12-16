import pandas as pd
import numpy as np
import math

#Küsin kasutajalt algselt millise koha infot ta soovib saada ja väljastab selle.
#Siis see programm leiab punktid ja aja optimaalsest sõnastikust
#Järgmisena programm küsib kasutajalt mitut inimest soovib graafikul näha
#kui see on väiksem 1 küsib uuesti kasutajalt
#Seejärel tuleb joongraafik ja mdea kas see üldse vastab su ootustele xd

#see teeb int sekundid minutiteks sõnena
def stom(aeg):
    if aeg % 60 < 10 or aeg % 60 == 0:
        if aeg/60 < 10 or aeg/60 < 1:
            return "0"+str(math.floor(aeg/60))+":0"+str(aeg%60)
        else:
            return str(math.floor(aeg/60))+":0"+str(aeg%60)
    else:
        if aeg/60 < 10 or aeg/60 < 1:
            return "0"+str(math.floor(aeg/60))+":"+str(aeg%60)
        else:
            return str(math.floor(aeg/60))+":"+str(aeg%60)

def graafikud(sõnastik):
    
    koht = input('Mitmenda koha infot soovite näha: ')
    
    inimene = sõnastik[koht]
    optimaalne = sõnastik["optimaalne"]
    
    print(inimene[0],"\nKoguaeg: "+stom(inimene[1])+"\nKaotus võitjale: "+
          stom(inimene[2]))
    print("etapiaeg\t\tparim etapiaeg")
    for i in range(3,len(inimene)):
        print(str(i-2)+". etapp: "+str(stom(inimene[i][1]))+" \t"+str(stom(optimaalne[i][1]))+"\tkaotus: "+str(inimene[i][1]-optimaalne[i][1])+" sekundit.")
    
    #äkki läheb vaja graafiku tegemisel, sest i have no idea
    """
    punktid = []
    aeg = []
    inimene_aeg = []
    for i in range(3,len(optimaalne)):
        punktid += [optimaalne[i][0]]
        aeg += [optimaalne[i][1]]
        inimene_aeg += [inimene[i][0]]
    """
    
    inimesed = int(input("Sisesta palju inimesi soovite graafikule: "))   
    
    while inimesed < 1:
        print("Ei saa leida")
        inimesed = int(input("Sisesta palju inimesi soovite graafikule: "))
    
    if inimesed == 1:
        üks_inimene = inimene_aeg
               
    
    """df = pd.DataFrame(np.random.randn(50, 4), 
            index=pd.date_range('1/1/2000', periods=50), columns=list('ABCD'))
    df = df.cumsum()
    df.plot(style='.-', markevery=5)"""
    