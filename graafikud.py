import matplotlib.pyplot as plt 
import numpy as np
import math

#Küsib kasutajalt algselt millise koha infot ta soovib saada ja väljastab selle.
#Siis see programm leiab punktid ja aja sõnastikust
#Seejärel tulevad joongraafikud

#see teeb int sekundid -> string minutid
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
          stom(inimene[2])+" ehk "+str(round(inimene[1]/sõnastik["1"][1],1))+"%")
    print("etapiaeg\t\tparim etapiaeg")
    for i in range(3,len(inimene)):
        print(str(i-2)+". etapp: "+str(stom(inimene[i][1]))+" \t"+str(stom(optimaalne[i][1]))+"\tkaotus: "
              +str(inimene[i][1]-optimaalne[i][1])+" sekundit.")
    
    z = 1
    punktid = [0]
    võitja = [0]
    inimene_koguaeg = [0]
    opt = [100]
    inimene_etapiaeg = [0]
    for i in range(3,len(optimaalne)):
        võitja += [sõnastik["1"][i][0]/60]
        inimene_koguaeg += [inimene[i][0]/60]
        opt += [optimaalne[i][1]]
        inimene_etapiaeg += [inimene[i][1]]
        punktid += [z]
        z += 1


    jooks = inimene_koguaeg
    
    
    
    #esimene graph
    plt.subplot(2, 1, 1)
    
    #esimene joon    
    y1 = võitja
    x1 = punktid
    plt.plot(x1, y1, color='green', linestyle='dashed', linewidth = 1, 
             marker='o', markerfacecolor='blue', markersize=4, label="võitja")    
    #teine joon    
    y2 = jooks
    x2 = punktid    
    plt.plot(x2, y2, color='red', linestyle='dashed', linewidth = 1, 
             marker='o', markerfacecolor='purple', markersize=4, label=koht+". koht")
    plt.ylim(0,round(max(y2)*1.2))
    plt.xlim(0,len(x1)) 
    plt.title('Võrldus võitjaga')
    plt.ylabel('aeg minutites')
    plt.legend()

    #teine graph
    plt.subplot(2, 1, 2)
    y3=[100]
    y4=[100]
    for i in range(1,len(opt)):
        y3.append(100)
        y4.append(opt[i]/inimene_etapiaeg[i]*100)
    #esimene joon    
    x3 = punktid
    plt.plot(x3, y3, color='green', linestyle='dashed', linewidth = 1, 
             marker='o', markerfacecolor='blue', markersize=4, label="optimaalne")    
    #teine joon
    x4 = punktid    
    plt.plot(x4, y4, color='red', linestyle='dashed', linewidth = 1, 
             marker='o', markerfacecolor='purple', markersize=4, label=str(koht+". koht"))
    plt.ylim(0,110)
    plt.xlim(0,len(x4))
    plt.xlabel('etapid')
    plt.ylabel('kaotus protsentides')
    plt.legend()
    
    
    
    
    plt.show()