# mus_tgbot

Для старта сервера:

1. Поднять ngrok на 5000 порту
2. Изменить переменную url на актуальную в app.py/start_bot
3. docker build -t mus-tgbot .
4. docker run -it -p 5000:5000 mus-tgbot
5. Перейти на http://localhost:5000/start_bot