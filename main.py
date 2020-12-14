from funktsioonid import read_html
from graafikud import*

def main():
    #klass = input("Sisesta võistlusklass: ")
    #url ='http://www.joka.ee/wp/wp-content/uploads/2020/10/tulemused_etapp_esialgne'
    url = "Tulemused.html"
    sõnastik = read_html(url)
    
    graafikud(sõnastik)
   

main()