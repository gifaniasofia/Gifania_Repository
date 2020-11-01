import pandas as pd
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request

class pembahasan_soal:
    
    def __init__(self, alamat):
        self.alamat = alamat
    
    def baca_data(self):
        html = urlopen(self.alamat)
        data = bs(html, 'html.parser')
        
        table = data.findAll('table', {'class': 'wikitable'})[0]
        rows = table.findAll('tr')
        
        hasil = []
        for row in rows:
            items = []

            for item in row.contents:
                try:
                    if item['colspan']:
                        status = False
                        break
                except:
                    status = True
                    
            hidelabel = row.findAll('span')
            for delete in hidelabel:
                delete.decompose()
            
            hidelabel_2 = row.findAll('sup')
            for delete_2 in hidelabel_2:
                delete_2.decompose()
            
            for cell in row.findAll(['td', 'th']):
                items.append(cell.get_text().strip())
                
            if status == True:
                hasil.append(items)
                
        df = pd.DataFrame(hasil)
        df.columns = df.iloc[0]
        df = df[1:]
        print(df)
        self.df = df
    
    def to_excel(self):
        data = self.df
        data.to_excel('table_list_of_brightest_stars.xlsx', index=False)

alamat = 'https://en.wikipedia.org/wiki/List_of_brightest_stars'
pembahasan = pembahasan_soal(alamat)
pembahasan.baca_data()
pembahasan.to_excel()
