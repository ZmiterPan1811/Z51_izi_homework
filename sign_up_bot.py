import telebot
import json

token = '_____________________________________________'

bot = telebot.TeleBot(token)

client_case = r'C:\projects\client_bot\clients'
name = ''
surname = ''
date_registracion = ''
time_registracion = ''
telephone_number = ''


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'записаться':
        bot.send_message(message.from_user.id, "Укажите Ваше имя")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, 'Напишите "записаться"')

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Укажите Вашу фамилию')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'На какую дату Вы хотите записаться?')
    bot.register_next_step_handler(message, get_date_registracion)

def get_date_registracion(message):
    global date_registracion
    date_registracion = message.text
    bot.send_message(message.from_user.id, 'На какое время Вы хотите записаться?')
    bot.register_next_step_handler(message, get_time_registracion)

def get_time_registracion(message):
    global time_registracion
    time_registracion = message.text
    bot.send_message(message.from_user.id, 'Укажите ваш номер телефона для обратной связи?')
    bot.register_next_step_handler(message, get_telephone_number)

def get_telephone_number(message):
    global telephone_number
    global client_data_id
    telephone_number = message.text
    client_data_id = {
        'Name': name,
        'Surname': surname,
        'Data': date_registracion,
        'Time': time_registracion,
        'Telephone': telephone_number,
        }
    file = open(f'clients\{surname}  {name}.txt', 'w', )
    file_in_json = json.dumps(client_data_id)
    lines = [f'в формате JSON {file_in_json}', f'в обычном формате {client_data_id}']
    for line in lines:
        file.write(line + '\n')
    file.close()
    bot.send_message(message.from_user.id, 'Спасибо! Наш сотрудник свяжется с вами в ближайшее время.')


bot.polling(none_stop=True, interval=0)
