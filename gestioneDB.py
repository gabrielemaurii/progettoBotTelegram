import csv
import requests
import requests
import mysql.connector
from mysql.connector import Error
import re
import itertools

class gestioneDB:
    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='', host='localhost', database='dbbot')
        self.cursor=self.conn.cursor()
            

    def insertImpianti(name):    
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='dbbot')
        cursor=conn.cursor()
        query="INSERT INTO impianti VALUES"
        with open(name, 'r') as file:
            reader = csv.reader(file)
            next(reader) # salto la prima riga (header)
            next(reader)
            for riga in reader:
                if(len(riga)==2):
                    rig=riga[0]+riga[1]
                    ##lista_senza_virgole = [campi.replace(",", "") for campi in rig] 
                    for field in rig:
                        v=field.split(";")
                        print(v)            
                        query+="('"+v[0]+"','"+v[1]+"','"+v[2]+"','"+v[3]+"','"+v[4]+"','"+v[5]+"','"+v[6]+"','"+v[7]+"','"+v[8]+"','"+v[9]+"')"
                        string=re.sub("/,","",query) 
                        cursor.execute(string)
                        query+=","
                else:
                    for field in riga:
                        v=field.split(";")
                        print(v)            
                        query+="('"+v[0]+"','"+v[1]+"','"+v[2]+"','"+v[3]+"','"+v[4]+"','"+v[5]+"','"+v[6]+"','"+v[7]+"','"+v[8]+"','"+v[9]+"')"
                        string=re.sub("/,","",query) 
                        cursor.execute(string)
                        query+=","


            conn.commit()


