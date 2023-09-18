import subprocess
import time
import os

# Список скриптов для мониторинга и перезапуска
scripts_to_monitor = ["pars.py", "sendtest1.py", "AutoSchick.py"]

while True:
    for script in scripts_to_monitor:
        # Проверка, активен ли процесс скрипта
        try:
            process = subprocess.Popen(["python", script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            process.communicate()  # Ожидание завершения скрипта

            # Если код завершения равен 0, скрипт успешно завершился
            if process.returncode == 0:
                print(f"Скрипт {script} успешно завершился.")
            else:
                print(f"Скрипт {script} завершился с ошибкой. Перезапуск...")
        except Exception as e:
            print(f"Ошибка при запуске скрипта {script}: {str(e)}")

    # Пауза на 5 секунд перед следующей проверкой
    time.sleep(5)

    # Проверка наличия интернет-соединения
    hostname = "google.com"
    response = os.system(f"ping -c 1 {hostname}")

    if response == 0:
        print("Интернет-соединение активно.")
    else:
        print("Интернет-соединение отсутствует. Ожидание подключения...")
        # Пауза и ожидание подключения к сети
        while response != 0:
            time.sleep(5)
            response = os.system(f"ping -c 1 {hostname}")
        print("Интернет-соединение восстановлено. Перезапуск скриптов.")
