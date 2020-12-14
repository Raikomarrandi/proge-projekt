from funktsioonid import read_html
def main():
    #klass = input("Sisesta võistlusklass: ")
    #url ='http://www.joka.ee/wp/wp-content/uploads/2020/10/tulemused_etapp_esialgne'
    url = "Tulemused.html"
    
    sõnastik = read_html(url)
    
    print(sõnastik["1"])
    print(sõnastik["optimaalne"])

main()

