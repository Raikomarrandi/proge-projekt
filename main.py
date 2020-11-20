from funktsioonid import read_html
def main():
    #klass = input("Sisesta võistlusklass: ")
    #url ='http://www.joka.ee/wp/wp-content/uploads/2020/10/tulemused_etapp_esialgne'
    url = "Tulemused.html"
    print(read_html(url))
    

main()
