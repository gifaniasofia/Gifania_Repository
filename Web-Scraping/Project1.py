from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
import pandas as pd

def kompas():
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14'
    headers = {'User-Agent': user_agent, 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

    alamat = 'https://www.kompas.com/'
    req = Request(alamat, headers=headers)
    html = urlopen(req)
    data = bs(html, 'html.parser')
    
    box = data.find('div',{'class':'most__wrap clearfix'})
    items = box.findAll('h4',{'class':'most__title'})
    
    hasil = [item.get_text() for item in items]
    
    df = pd.DataFrame(hasil, columns=['Berita Terpopuler'])
    print(df)
    
kompas()
