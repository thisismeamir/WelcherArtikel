import requests
from bs4 import BeautifulSoup

class wordClass():
    def __init__(self,word):
        self.Word = word
        self.Artikel = wordClass.requestWordArtikel(word)
    
    def requestWordArtikel(self):
        artikel = ["der","die","das"]
        for i in artikel:
            if requests.get(f"https://der-artikel.de/{i}/{self.Word}.html").ok:
                return i
            else:
                continue
        return 'None'
    