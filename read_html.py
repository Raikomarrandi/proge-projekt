import urllib.request
from bs4 import BeautifulSoup as bs

#nendest põhimõtteid veits
#https://www.codementor.io/@phamvan/simple-way-to-get-data-from-web-page-using-python-q9f85jkin
#crummy.com/software/BeautifulSoup/bs4/doc/


#http://www.okvoru.ee/site/wp-content/uploads/2020/09/EMV_tavarada050920_etapid_a1.htm seda oleks vaja lugeda


fp = urllib.request.urlopen("https://docs.python.org/3/howto/urllib2.html") ## pm mdea see ei lugenud tulemuste html-i
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)