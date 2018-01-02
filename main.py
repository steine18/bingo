import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, timedelta
from db import Cashball



def db_entry(casino, datetime, dollar):
    query = (Cashball.select().where((Cashball.casino == str(casino)) &
                                     (Cashball.datetime == str(datetime)) &
                                     (Cashball.dollar == int(dollar))))
    if len(query) == 0:
        entry = Cashball(casino=casino, datetime=datetime, dollar=dollar, record_time=str(datetime.now()))
        entry.save()
        print('Save')
    else:
        print('Done')
        pass


def update_cashball():
    r = requests.get('http://www.fiestacasinobingo.com')
    soup = BeautifulSoup(r.content, 'html.parser')
    now = datetime.now()
    for row in range(2, 11):
        game = soup.table.find_all('tr')[row]
        time = datetime.strptime(game.find_all('td')[0].get_text(), '%I%p')
        time = f'{str(now.date())} {str(time.time())}'
        time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        if time >= now:
            time = time - timedelta(days=1)
        try:
            rancho = int(re.sub('[^0-9]', '', game.find_all('td')[1].get_text()))
            db_entry('rancho', time, rancho)
        except ValueError:
            pass
        try:
            henderson = int(re.sub('[^0-9]', '', game.find_all('td')[4].get_text()))
            db_entry('henderson', time, henderson)
        except ValueError:
            pass


update_cashball()
