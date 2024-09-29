import telebot

bot = telebot.TeleBot('')
types = telebot.types

@bot.message_handler(commands=['id'])
def echo_message(message):

    chat_id = message.chat.id

    try:
        msg_thread_id = message.reply_to_message.message_thread_id
    except AttributeError:
        msg_thread_id = "General"

    bot.reply_to(message, f"Индетификатор темы: {msg_thread_id}")


@bot.message_handler(content_types=['text'])
def poll(message):

    if message.text.lower() == 'опрос':
        chat_id = '-1002212292832'
        theard_id = message.message_thread_id

        bot.send_poll(chat_id, question='Кто будет завтра?', options=['Я буду', 'Меня не будет', 'Не знаю'], is_anonymous=False, message_thread_id= theard_id)

    print(f'{message} \n {message.text}')



bot.infinity_polling()
