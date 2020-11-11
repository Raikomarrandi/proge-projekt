import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
url = 'http://www.okvoru.ee/site/wp-content/uploads/2020/09/EMV_tavarada050920_etapid_a1.htm'


response = http.request('GET', url)
soup = BeautifulSoup(response.data,'html.parser')


print(soup.title)
print(soup.a)
print(soup.b)

#4h mässamist, 100 lehte läbi lapatud ja lõpuks peaks korras olema :)))))))
