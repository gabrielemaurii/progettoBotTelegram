import requests
import json


class Telegram:
    def __init__(self):
        self.bot_token ="6224212161:AAF5mEaA_c18e_eciCn77cX2aj1ubj8L350"
        self.base_url = f'https://api.telegram.org/bot{self.bot_token}'
        self.ultimo_msg=0
        #self.utlimo_msg

    def get_updates(self):
        response = requests.get(f'{self.base_url}/getUpdates')
        if response.status_code == 200:
            data = response.json()
            if data['ok']:
                Telegram.process_response(data)
                
                
                ## controllo che c'è un messaggio nuovo con update_id
            else:
                print("Errore nella richiesta")
        else:
            print("Errore nella connessione")

    def send(self,chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        response = requests.get(f'{self.base_url}/sendMessage', params=params)
        if response.status_code == 200:
            data = response.json()
            return data.get('result')
        return None
        
    
    def process_response(response,ultimomsg=0):
        t=Telegram()
        
        if 'result' in response:
            messages = response['result']
            for message in messages:
                # Accedi ai campi del messaggio
                update_id=message['update_id']
                
                message_id = message['message']['message_id']
                chat_id = message['message']['chat']['id']
                if 'text' in message['message']:
                    text = message['message']['text']
                    print(f"Text: {text}")
                elif 'location' in message['message']:
                    latitude=message['message']['location']['latitude']
                    longitude=message['message']['location']['longitude']
                    print(f"latitude: {latitude}")
                    print(f"longitude: {longitude}")  
                if(update_id>ultimomsg):
                    ultimomsg=update_id                
                    t.send(chat_id,'ciao')
                    

                # Esempio di elaborazione del messaggio
                print(f"Message ID: {message_id}")
                print(f"update_id: {update_id}")
                print(f"Chat ID: {chat_id}")               
                print("--------------------")               
                

        


# Esempio di utilizzo

