from bs4 import BeautifulSoup
import requests

def buscarComic(buscar = ''):
    html = requests.get(f"https://getcomics.org/?s={buscar}")
    soup = BeautifulSoup(html.text,'html.parser')
    links = soup.find_all('a')
    listaDeLinks = []
    for link in links:
        if link.get('href') != None and buscar in link.get('href'):
            listaDeLinks.append(link.get('href'))

        else:
            continue

    return listaDeLinks
