import json
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys

def process_links(links, processed_links):
    # Установка пути к драйверу Chrome
    chromedriver_path = '/home/name/dr/chromedriver'  # Укажите правильный путь к chromedriver

    # Инициализация драйвера Chrome с DevTools Protocol
    options = ChromeOptions()
    options.debugger_address = 'localhost:9222'  # Укажите порт отладки Chrome, где запущен активный браузер
    driver = webdriver.Chrome(service=ChromeService(executable_path=chromedriver_path), options=options)

    # Проход по каждой ссылке и нажатие кнопки
    for link in links:
        zum_formular_link = link.get('Zum Formular')
        if zum_formular_link and zum_formular_link not in processed_links:
            process_link(driver, zum_formular_link)
            processed_links.append(zum_formular_link)

    # Закрытие браузера
    driver.quit()

def process_link(driver, link):
    # Открытие новой вкладки
    driver.execute_script("window.open();")
    # Переключение на новую вкладку
    driver.switch_to.window(driver.window_handles[-1])

    # Открытие страницы
    driver.get(link)

    # Ваш код для обработки страницы здесь

    # Добавляем ожидание в 3 секунды перед нажатием кнопки
    time.sleep(3)

    # Нажатие на кнопку "jetzt bewerbung" через выполнение JavaScript-кода
    driver.execute_script('document.querySelector(\'div.application-actions__actions app-button button\').click()')

    # Добавляем ожидание в 3 секунды после нажатия кнопки
    time.sleep(3)

if __name__ == '__main__':
    # Проверка наличия файла zum_messages.json
    if not os.path.exists('zum_messages.json'):
        print("Файл 'zum_messages.json' не найден.")
    else:
        # Чтение JSON из файла zum_messages.json
        with open('zum_messages.json', 'r') as f:
            links = json.load(f)

        # Проверка наличия файла zum_messagesberait.json
        if os.path.exists('zum_messagesberait.json'):
            with open('zum_messagesberait.json', 'r') as f:
                processed_links = json.load(f)
        else:
            processed_links = []

        process_links(links, processed_links)
