import requests
from bs4 import BeautifulSoup

html_doc= requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})

soup = BeautifulSoup(html_doc.text, 'html.parser')

populer_area = soup.find(attrs={'class': 'grid-row list-content'})

titles = populer_area.findAll(attrs={'class': 'media__title'})#mencari keseluruhan khusus dalam media_titles dalam
# bentuk list
images = populer_area.findAll(attrs={'class': 'media__image'})

#for title in titles: # untuk pencarian bersih satu persatu dan hanya title text yang di munculkan
    #print(title.text)

for image in images:
    print(image.find('a').find('img')['title'])#mencari gambar dan list nama berita
#print(titles)
