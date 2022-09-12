from bs4 import BeatifulSoup
import requests

# Carrega a pagina com informacoes sobre o clima
html = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp").content

# Faz o parser do html da pagina
soup = BeatifulSoup(html, 'html.parser')

# Captura dados navegando nos elementos do html
resume = soup.find(class_='gray -line-height-24 _center')
tempMin = soup.find(id='min-temp-1')
tempMax = soup.find(id='max-temp-1')

# Mostra os resultados
print('\n Resumo: ' + resume.text)
print(' Temp. Minima: ' + tempMin.string)
print(' Temp. Maxima: ' + tempMax.string)