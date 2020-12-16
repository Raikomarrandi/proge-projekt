from funktsioonid import read_html
from graafikud import *

def main():
    
    url = "Tulemused.html"
    
    sõnastik = read_html(url)
    
    graafikud(sõnastik)
   

main()