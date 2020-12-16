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
    #ülejäänud listi elemendid on järjestatult etapid ennikutena (etapiaeg, koguaeg etapi lõpus)
#võistlejad{"optimaalne"}
    #list[0] on pealkiri, list[1] on parimate etapiaegade summa (optimaalne koguaeg) ja list[2] on vahe võitjaga
    #list, kus lähevad järjest kõikide etappide võiduajad ennikutena formaadis (etapiaeg, koguaeg etapi lõpus)

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
                elif isik[x][3] == ":":
                    aeg = int(isik[x][0]+isik[x][1]+isik[x][2])*60 + int(isik[x][4]+isik[x][5])
                koht= int(isik[x][-3]+isik[x][-2])
                võistleja.append(aeg)
                    
            #aeg ja koht on eraldi
            elif isik[x][-1] == "(":
                if isik[x][2] == ":":
                    aeg = int(isik[x][0]+isik[x][1])*60 + int(isik[x][3]+isik[x][4])
                elif isik[x][1] == ":":
                    aeg = int(isik[x][0])*60 + int(isik[x][2]+isik[x][3])
                if isik[x+1][-1] == ")" and len(isik[x+1]) <= 2:
                    koht = int(isik[x+1][0])
                võistleja.append(aeg)

        võistlejad[str(i+1)] = võistleja
     
    #arvutab koguaja ja kaotuse võistlejatel
    võitja_aeg = võistlejad["1"][-1]
    võistlejad["1"][1] = võitja_aeg
    võistlejad["1"][2] = 0
    for i in range(2,len(võistlejad)):
        try:
            koguaeg = võistlejad[str(i)][-1]
            kaotus = koguaeg - võitja_aeg
            võistlejad[str(i)][1] = koguaeg
            võistlejad[str(i)][2] = kaotus
        except:
            koguaeg= "DNF"
            kaotus = "Puudub"
        
    #lisab võistlejatele mittekommutatiivsed etapiajad
    for i in võistlejad:
        if i != "optimaalne":
            for el in range(len(võistlejad[i])-4):
                võistlejad[i][-el-1] = (võistlejad[i][-el-1], võistlejad[i][-el-1] - võistlejad[i][-el-2])
            try:
                võistlejad[i][3] = (võistlejad[i][3],võistlejad[i][3])
            except:
                pass
    #leiab iga etapi parima (optimaalse) aja
    opt_aeg = 0
    for etapp in range(3,len(võistlejad["1"])):
        etapiajad=[]
        for i in võistlejad:
            #print(võistlejad[i][etapp])
            try:
                etapiajad.append(võistlejad[i][etapp][1])
            except:
                pass
        opt_aeg += min(etapiajad)
        optimaalne.append((opt_aeg,min(etapiajad)))
    kaotus = opt_aeg - võitja_aeg
    võistlejad["optimaalne"] = ["Optimaalne",opt_aeg,kaotus] + optimaalne
          
    return võistlejad