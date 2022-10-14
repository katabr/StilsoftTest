# StilsoftTest
Test task on position QA in Stilsoft

Файл list_of_card.txt содержт список всех карточек на странице https://stilsoft.ru/products/kitsoz-synerget
Файл results.txt содержит список карточек по заданию (таковых не оказалось)
В папке Video Test находится видео запуска автотеста

Тест запускался на локальном окружении
Версии ПО:
- Python 3.8.2;
- Selenium 3.14;
- Pytest 7.1.3;

Версия браузера:
- Chrome 106.0/5249.103(64 бит)
- Chromedriver 106.0.5249.61

Зависимости окужения в файле requirements.txt

Запуск:
1. Настроить окружение
2. Установить зависимости
3. Запуск через терминал из папки StilsoftTest командой pytest -v test_cards.py
