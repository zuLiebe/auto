import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
import schedule
import time

BASE_URL = 'https://www.saga.hamburg'

def scrape_website():
    url = urljoin(BASE_URL, '/immobiliensuche?type=wohnungen')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    listings = soup.select('div.teaser3.teaser3--listing.teaser-simple--boxed')

    data_list = []

    for listing in listings:
        link = listing.select_one('a.inner')['href']
        absolute_link = urljoin(BASE_URL, link)  # Construct the absolute URL
        listing_response = requests.get(absolute_link)
        listing_soup = BeautifulSoup(listing_response.text, 'html.parser')

        details = listing_soup.select('dl.dl-props')

        objektnummer = get_value(details, 'Objektnummer')
        netto_miete = get_value(details, 'Netto-Kalt-Miete')
        gesamtmiete = get_value(details, 'Gesamtmiete')
        zimmer = get_value(details, 'Zimmer')
        verfugbar_ab = get_value(details, 'Verfügbar ab')

        # Извлекаем ссылку на "Zum Formular"
        formular_link = listing_soup.find('a', href=True, text='Zum Formular')
        if formular_link:
            formular_link = urljoin(BASE_URL, formular_link['href'])

        # Создание словаря с извлеченными данными, включая ссылку на "Zum Formular"
        data = {
            'Objektnummer': objektnummer,
            'Netto-Kalt-Miete': netto_miete,
            'Gesamtmiete': gesamtmiete,
            'Zimmer': zimmer,
            'Verfügbar ab': verfugbar_ab,
            'Link': absolute_link,
            'Zum Formular': formular_link,  # Добавляем ссылку на "Zum Formular"
        }

        data_list.append(data)

    # Сохранение данных в файл
    with open('data.json', 'w') as f:
        json.dump(data_list, f)

    # Запись результатов в лог
    with open('log.txt', 'a') as log_file:
        log_file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - Scraped {len(data_list)} listings\n')

def get_value(details, label):
    element = details[0].find('dt', text=label)
    if element:
        return element.find_next('dd').get_text(strip=True)
    return ''

def schedule_scraping():
    schedule.every(9).seconds.do(scrape_website)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    schedule_scraping()
