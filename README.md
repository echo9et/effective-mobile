# Для запуска проекта
```
docker compose up -d --build 
```
# Проверка статуса
```
docker compose ps
```

# Проверка работы
```
curl http://localhost
```

GET запрос приходит на nginx, котоырй слушает 80 порт. \
Далее открывает новое соединения с backend, подписывает заголовки и отправляет запрос. \
Получает ответ от backend на запрос и напралвяет ответ потребителю. \

# Схема взаимодействия

request -> 
nginx -> proxy_pass http://backend:$(BACKEND_PORT) -> FLASK (0.0.0.0:$(BACKEND_PORT)) 
-> response