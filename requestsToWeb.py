from os import stat
import requests
from bs4 import BeautifulSoup

class wordInstance():
    
    wordKomp = ""
    def __init__(self,word):
        self.Word = word
        self.Artikel = self.requestWordArtikel(word)
    
    def Meaning(self):
        html_temp = requests.get("https://der-artikel.de/{0}/{1}.html".format(self.Artikel,self.Word)).text
        soup = BeautifulSoup(html_temp, 'lxml')
        meaning = soup.find("h3", class_="mb-5").text
        meaning = meaning.replace(" ","")
        printable = ""

        return meaning
        
    
    def requestWordArtikel(self,Word):
        artikel = ["der","die","das"]
        for i in artikel:
            if requests.get(f"https://der-artikel.de/{i}/{Word}.html").ok:
                artikelFound = True
                return i
            else:
                artikelFound = False
        if not artikelFound:
            KopositionArtikel = wordInstance.KopositionFounder(Word)

            if KopositionArtikel != "None":
                return KopositionArtikel
            else:
                return 'None'

    @staticmethod
    def KopositionFounder(word):
        Counter = 0
        wordInstance.wordKomp = ""
        while Counter < len(word):
            Counter += 1
            wordInstance.wordKomp =   word[-Counter] + wordInstance.wordKomp
            checkWord = wordInstance.wordKomp
            artikel = ["der","die","das"]
            for i in artikel:
                if requests.get(f"https://der-artikel.de/{i}/{checkWord}.html").ok:
                    wordInstance.wordKomp = ""
                    return i
                else:
                    continue    
        return "None"
    
    def TableComposer(self, Artikel):
        if Artikel != "None":
            html_in = requests.get(f"https://der-artikel.de/{Artikel}/{self.Word}.html").text
            soup = BeautifulSoup(html_in,'lxml')
            table = soup.find('table', class_='table').text
            table = table.split("\n")
            newtable = []
            printable=""
            for i in table:
                if i != '':
                    newtable.append(i)
            newtable.insert(0,"")
            j = 0
            max1 = len(newtable[0])
            for i in newtable:
                
                if len(i) > max1:
                    max1 = len(i)
                else:
                    continue
            
            i = 1
            while i < len(newtable)+1:
                printable = printable + f"{newtable[i - 1]:{max1}}" + " - "
                if i%3 == 0:
                    printable = printable + "\n\n"
                
                i+=1



            #for i in newtable:
                
            #    if j == 3:
            #        j = 0
            #        printable = printable+ "\n" + "-----------------------------" +"\n" + f"{i}"  
            #    else:
            #        printable = printable+ f"{i}"  + " | "
            ###        j += 1
            
            return printable
        else:
            return "None"

word = wordInstance("Apfel")
word.Meaning() 