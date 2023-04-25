import requests

url = 'https://www.mise.gov.it/images/exportCSV/anagrafica_impianti_attivi.csv'
response = requests.get(url)

with open('bot_/impianti.csv', 'wb') as f:
    f.write(response.content)
