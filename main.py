from telethon import TelegramClient, events  # Імпортуємо потрібні бібліотеки

api_id = 22271921  # Вводимо id нашого телеграм клієнта, та записуємо номер щоб не загубити +380673418119
api_hash = 'ccbe6ee4953cef67353ec0a0e2b8d8ee'  # Вводимо hash нашого телеграм клієнта

client = TelegramClient("Test", api_id, api_hash)  # Збираемо клієнта до купи
target_can = -1001734796210  # Вводимо id в який будемо пересилати повідомлення
key_words = ["Повітряна тривога", "Відбій тривоги"]  # Вводимо ключові слова які будемо шукати в повідомленнях


@client.on(events.NewMessage(
    chats=[-1001505028797, -1001734796210]))  # Запускаємо наш клієнт та сказуемо на які саме канали реагувати
async def normal_handler(event):  # Обробляємо подію
    for i in range(len(key_words)):  # Перебираємо всі ключові слова з нашого списку
        if key_words[i] in event.message.message:  # Перевіряємо коне слово на наявність його в нашому повідомленні
            print(event.message)
            print(event.message.peer_id,
                  event.message.message)  # Роздруковуемо в консоль id чату/групи та текст знайденного повідомлення (не обов'язково)
            await client.send_message(target_can, event.message)  # Пересилаємо знайдене повідомлення


client.start()  # Запускаємо кліент
client.run_until_disconnected()  # Ставимо його в бескінечний цикл