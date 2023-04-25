import csv
import sqlite3

# Configurazione della connessione al database MySQL

conn = sqlite3.connect('bottelegram')
cursor = conn.cursor()

# Apertura del file CSV e inserimento dei dati nel database
with open('bot_/prezzi.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        cursor.execute('INSERT INTO prezzi (ID, gestore,bandiera,tipoImpianto,nomeImpianto,indirizzo,comune,provincia,latitudine,longitudine) VALUES (?, ?,?,?,?,?,?,?,?,?)', row)

# Commit delle modifiche e chiusura della connessione
conn.commit()
conn.close()