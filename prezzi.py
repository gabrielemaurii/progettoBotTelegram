import requests

url = 'https://www.mise.gov.it/images/exportCSV/prezzo_alle_8.csv'
response = requests.get(url)

with open('bot_/prezzi.csv', 'wb') as f:
    f.write(response.content)
    
