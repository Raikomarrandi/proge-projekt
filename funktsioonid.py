import urllib3
from bs4 import BeautifulSoup

#siin failis abifunktsioonid

#url for testing = 'http://www.okvoru.ee/site/wp-content/uploads/2020/09/EMV_tavarada050920_etapid_a1.htm'
#file:///C:/Users/Raiko/Desktop/T%C3%9C%20proge/proge-projekt/Tulemused.html

def read_html(url):
    html_doc = open("Tulemused.html",encoding="utf-8")
    soup = BeautifulSoup(html_doc,'html.parser')
    soup = soup.find("pre")
    [x.extract() for x in soup.select('span')]
    aba = soup.getText()
    aba = aba.split("\n")
    for i in aba:
        if i == "" or i == " ":
            aba.remove(i)
    võistlejad={}
    for i in range(len(aba)):
        vend = aba[i].split()
        võistlejad[str(i+1)] = vend[1:]
    return võistlejad["1"]