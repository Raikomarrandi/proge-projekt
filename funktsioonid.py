import urllib3
from bs4 import BeautifulSoup
from string import digits

#siin failis abifunktsioonid

#url for testing = 'http://www.okvoru.ee/site/wp-content/uploads/2020/09/EMV_tavarada050920_etapid_a1.htm'
#file: "Tulemused.html"

## võistlejad{} instructions ##

# järjestatud koha järgi, nt võistlejad{"1"} on võitja
    #info võistlejate kohta listina
    #list[0] on nimi+klubi, list[1] on koguaeg, list[2] on kaotus võitjale
    #ülejäänud listi elemendid on järjestatult etapid ennikutena (aeg sekundites, koht etapil)
#võistlejad{"optimaalne"}
    #list[0] on pealkiri, list[1] on parimate etapiaegade summa (optimaalne koguaeg) ja list[2] on vahe võitjaga
    #list, kus lähevad järjest kõikide etappide võiduajad ennikutena formaadis (etapinr, etapiaeg)

####

def read_html(url):
    html_doc = open(url,encoding="utf-8")
    soup = BeautifulSoup(html_doc,'html.parser')
    soup = soup.find("pre")
    [x.extract() for x in soup.select('span')]
    test = soup.getText()
    test = test.split("\n")
    for i in test:
        if i == "" or i == " ":
            test.remove(i)
    võistlejad={}
    optimaalne=[]
    
    #SLICING:
    for i in range(len(test)):
        isik = test[i].split()
        isik = isik[1:]
        
        nimi=""
        eemaldada=[]
        for el in isik:
            #(nimi+klubi) üheks stringiks
            if el[0].isdigit()== False and el[0] != "+" and el != "Puuduv" and el != "KP":
                eemaldada.append(el)
                nimi += ''.join(el)+" "
                
        #nimi+klubi järjendisse sisse, vanad elemendid välja
        for element in eemaldada:
            isik.remove(element)
        võistleja = [nimi] + isik[:2]
        
        #etapiaeg+koht
        for x in range(2,len(isik)):
            
            #kahekohalise arvuga koht ehk koos on aeg + koht
            if isik[x][-1] == ")" and len(isik[x]) > 2:
                if isik[x][2] == ":":
                    aeg = int(isik[x][0]+isik[x][1])*60 + int(isik[x][3]+isik[x][4])
                elif isik[x][1] == ":":
                    aeg = int(isik[x][0])*60 + int(isik[x][2]+isik[x][3])
                koht= int(isik[x][-3]+isik[x][-2])
                võistleja.append((aeg,koht))
                if koht == 1:
                    optimaalne.append((len(võistleja)-3,aeg-võistleja[-1][0]))
                    
            #aeg ja koht on eraldi
            elif isik[x][-1] == "(":
                if isik[x][2] == ":":
                    aeg = int(isik[x][0]+isik[x][1])*60 + int(isik[x][3]+isik[x][4])
                elif isik[x][1] == ":":
                    aeg = int(isik[x][0])*60 + int(isik[x][2]+isik[x][3])
                if isik[x+1][-1] == ")" and len(isik[x+1]) <= 2:
                    koht = int(isik[x+1][0])
                võistleja.append((aeg,koht))
                if koht == 1:
                    if type(võistleja[-2][0]) == int:
                        optimaalne.append((len(võistleja)-3,aeg-võistleja[-2][0]))
                    else:
                        optimaalne.append((len(võistleja)-3,aeg))

        võistlejad[str(i+1)] = võistleja
    
    #arvutab optimaalse koguaja ja vahe võitjaga
    parim_aeg=0
    for i in range(3,len(optimaalne)):
        parim_aeg += int(optimaalne[i][1])
    võitja_aeg = võistlejad["1"][1]
    kaotus=0
    if len(võitja_aeg) == 8:
        võitja_aeg = (int(võitja_aeg[0] + võitja_aeg[1])*60*60 + int(võitja_aeg[3] + võitja_aeg[4])*60 + int(võitja_aeg[6] + võitja_aeg[7]))
        kaotus = parim_aeg - võitja_aeg
    elif len(võitja_aeg) == 6:
        võitja_aeg = (int(võitja_aeg[0] + võitja_aeg[1])*60 + int(võitja_aeg[3] + võitja_aeg[4]))
        kaotus = parim_aeg - võitja_aeg
    elif len(võitja_aeg) == 7:
        võitja_aeg = (int(võitja_aeg[0])*60*60 + int(võitja_aeg[2] + võitja_aeg[3])*60 + int(võitja_aeg[5] + võitja_aeg[6]))
        kaotus = parim_aeg - võitja_aeg
        
    võistlejad["optimaalne"] = ["Optimaalne",parim_aeg,kaotus] + sorted(optimaalne)
    
    #arvutab koguaja ja kaotuse võistlejatel
    võistlejad["1"][1] = võitja_aeg
    võistlejad["1"][2] = 0
    for i in range(2,len(võistlejad)):
        try:
            koguaeg = võistlejad[str(i)][1]
            if len(koguaeg) == 8:
                koguaeg = (int(koguaeg[0] + koguaeg[1])*60*60 + int(koguaeg[3] + koguaeg[4])*60 + int(koguaeg[6] + koguaeg[7]))
                kaotus = võitja_aeg - koguaeg
            elif len(koguaeg) == 6:
                koguaeg = (int(koguaeg[0] + koguaeg[1])*60 + int(koguaeg[3] + koguaeg[4]))
                kaotus = võitja_aeg - koguaeg
            elif len(koguaeg) == 7:
                koguaeg = (int(koguaeg[0])*60*60 + int(koguaeg[2] + koguaeg[3])*60 + int(koguaeg[5] + koguaeg[6]))
                kaotus = võitja_aeg - koguaeg
            võistlejad[str(i)][1] = koguaeg
            võistlejad[str(i)][2] = kaotus
        except:
            pass
    
    return võistlejad