import requests
from bs4 import BeautifulSoup
from csv import writer

url='https://www.pararius.com/apartments/amsterdam'
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
lists=soup.find_all('section',class_='listing-search-item')

with open('housing.csv','w', encoding='utf8', newline='') as f:
    thewriter= writer(f)
    header=['TITLE', 'ADDERESS', 'PRICE', 'AREA']
    thewriter.writerow(header)

    for list in lists:
        title=list.find('a',class_='listing-search-item__link listing-search-item__link--title').get_text(strip=True)
        address=list.find('div',class_='listing-search-item__sub-title').get_text(strip=True)
        price=list.find('div',class_='listing-search-item__price').get_text(strip=(True))
        area=list.find('li',class_='illustrated-features__item illustrated-features__item--surface-area').get_text(strip=(True))
        info=[title,address,price,area]
        thewriter.writerow(info)
