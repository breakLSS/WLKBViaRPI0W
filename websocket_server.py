from websocket_server import WebsocketServer

# Эта функция будет вызываться при подключении нового клиента
def new_client(client, server):
    print(f"New client connected: {client['address']}")
    server.send_message_to_all("Welcome new client!")

# Эта функция будет вызываться, когда клиент отправляет сообщение
def message_received(client, server, message):
    print(f"Message from client: {message}")
    server.send_message_to_all(f"Client says: {message}")

# Создаем сервер на порту 8080
server = WebsocketServer(8080, host='0.0.0.0')

# Указываем обработчики событий
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)

# Запускаем сервер
print("Server started...")
server.run_forever()
