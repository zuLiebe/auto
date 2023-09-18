import json
from aiogram import Bot, types
import asyncio

# Вставьте свой токен бота и ID чата
bot_token = '6460057618:AAHMX4f9ba--_tQ_FbIaJIgbU0i0GfIhvl8'
chat_id = '-1001973489502'

async def send_to_telegram():
    # Чтение данных из файла
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Загрузка ранее отправленных объектов
    sent_objects = load_sent_objects()

    # Фильтрация новых объектов
    new_objects = filter_new_objects(data, sent_objects)

    # Отправка сообщений в Telegram
    if new_objects:
        bot = Bot(token=bot_token)
        for item in new_objects:
            message = format_message(item)
            await bot.send_message(chat_id=chat_id, text=message)

        # Сохранение отправленных объектов после успешной отправки
        save_sent_objects(sent_objects, new_objects)

        # Сохранение всех отправленных сообщений в JSON-файле
        save_messages_to_json(new_objects)

def format_message(item):
    message = f"Objektnummer: {item['Objektnummer']}\n"
    message += f"Netto-Kalt-Miete: {item['Netto-Kalt-Miete']}\n"
    message += f"Gesamtmiete: {item['Gesamtmiete']}\n"
    message += f"Zimmer: {item['Zimmer']}\n"
    message += f"Verfügbar ab: {item['Verfügbar ab']}\n\n"
    message += f"Link: {item['Link']}\n"
    formular_link = item.get('Zum Formular')
    if formular_link:
        message += f"Ссылка на Zum Formular: {formular_link}\n"
    return message.strip()

def load_sent_objects():
    try:
        with open('sent_objects.json', 'r') as f:
            sent_objects = json.load(f)
    except FileNotFoundError:
        sent_objects = []
    return sent_objects

def filter_new_objects(data, sent_objects):
    new_objects = []
    for item in data:
        if item['Objektnummer'] not in sent_objects:
            new_objects.append(item)
    return new_objects

def save_sent_objects(sent_objects, new_objects):
    # Обновляем список отправленных объектов
    sent_objects.extend([item['Objektnummer'] for item in new_objects])
    with open('sent_objects.json', 'w') as f:
        json.dump(sent_objects, f)

def save_messages_to_json(messages):
    with open('zum_messages.json', 'w') as f:
        json.dump(messages, f, indent=4)

async def schedule_sending():
    while True:
        await send_to_telegram()
        await asyncio.sleep(5)  # Ожидание 5 секунд перед повторным выполнением

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(schedule_sending())
