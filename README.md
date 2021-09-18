# mus_tgbot

Для старта сервера:

1. Поднять ngrok на 5000 порту
2. docker build -t mus-tgbot .
3. docker run -it -e TOKEN='{token}' -p 5000:5000 mus-tgbot
4. Перейти на http://localhost:5000/start_bot, вставить туда ссылку ngrok
