import requests,bs4
import csv

base_url = 'https://www.iplt20.com/teams/men'
res = requests.get(base_url)
soup = bs4.BeautifulSoup(res.text,'lxml')

def ipl_data():
    product_card = soup.select('.card__details')
    product_title = soup.select('.card__title')
    product_subtitle = soup.select('.card__subtitle')
    product_year = soup.select('.team-card__wins')
    win_year = []
    j = 0
    i = 0
    while j < len(product_title):
        if product_card[j].find('div'):
            if i<len(product_year):
                win_year.append(product_year[i].get_text().strip())
                i+=1
            j+=1
        else :
            win_year.append('Not win yet')
            j+=1

    team_data_dictionary = {}
    for i in range(1,9):
        team_data_dictionary[f'{i}'] = {}
    for i in range(8):
        team_data_dictionary[f'{i+1}']['title'] = product_title[i].getText()
        team_data_dictionary[f'{i+1}']['venue'] = product_subtitle[i].getText().strip()
        team_data_dictionary[f'{i+1}']['winning_year'] = win_year[i]


    return team_data_dictionary