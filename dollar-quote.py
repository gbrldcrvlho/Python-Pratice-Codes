import requests

# Link publico com valor atual da cotacao do dolar
url = 'https://economia.awesomeapi.com.br/all/USD-BRL'

# Busca os dados
response = requests.get(url)

# Se a busca funcionou, mostra o valor
if response.status_code == 200:
    dolar_value = response.json()['USD']['low']
    print(f'O valor atual do Dolar e de R${dolar_value}')
else:
    print('Erro ao buscar o valor do Dolar!')