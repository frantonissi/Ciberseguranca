import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url_base = "https://store.steampowered.com/?l=portuguese"

pagina = requests.get(url_base) #visitar um site

soup = BeautifulSoup(pagina.text, "html.parser") #“Pegue o HTML bruto da página e transforme em uma estrutura organizada que eu consigo navegar e buscar elementos.”

links = soup.find_all("a")

for link in links: #Dentro do loop, cada tag <a> se comporta como um dicionário do Python. Podemos pegar o atributo href usando colchetes, assim: link['href'].
    
    # 'link' é cada item <a>, um de cada vez
    # Agora pegamos o 'href' do item atual
    
    #Temos as tags <a>, mas não queremos a tag inteira. Nós só queremos o link de verdade, que está no atributo href.
    
    href_original = link['href']
    
    if href_original: # Só processa se o 'href' existir
        href_consertado = urljoin(url_base, href_original)
        print(href_consertado)

print("\n--- Extração concluída ---")