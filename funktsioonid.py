import urllib3
from bs4 import BeautifulSoup

#siin failis abifunktsioonid

#url for testing = 'http://www.okvoru.ee/site/wp-content/uploads/2020/09/EMV_tavarada050920_etapid_a1.htm'
def read_html(url):
        http = urllib3.PoolManager()


        response = http.request('GET', url)
        soup = BeautifulSoup(response.data,'html.parser')


        print(soup.title)
        print(soup.a)
        print(soup.b)
