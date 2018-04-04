import requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image

search_term = input('Enter Search term')
params = {'q': 'football'}
r = requests.get('https://www.google.co.in/search', params=params)

soup = BeautifulSoup(r.text, 'html5lib')

links = soup.find('div', id='search')
links = links.find_all('img')
results = [link['src'] for link in links if "/maps" not in link['src']]

link = results[0]
if ("encrypted" not in link):
    link = link[:link.find('?')]

r = requests.get(link)
image = Image.open(BytesIO(r.content))
image.save()