import undetected_chromedriver.v2 as uc
from config import *  # Se importa el token de telegram
import telebot  # Para manejar la api de telegram
import time
import threading # Multitarea
from telebot.types import ReplyKeyboardMarkup # Para crear botones
from telebot.types import ForceReply # Para citar un mensaje
# Se instancia el bot de telegram
bot = telebot.TeleBot(telegram_token)
# Variable global
producto = {}


# Responde al comando /start
@bot.message_handler(commands=["start"])
def cmd_start(message):
    # Da la bienvenida al usuario del bot.
    print(message.chat.id)
    x = bot.reply_to(message, "Iniciando", )
    time.sleep(1)
    bot.edit_message_text("Iniciando 🟩", message.chat.id, x.message_id)
    time.sleep(1)
    bot.edit_message_text("Iniciando 🟩🟩", message.chat.id, x.message_id)
    time.sleep(1)
    bot.edit_message_text("Iniciando 🟩🟩🟩", message.chat.id, x.message_id)
    time.sleep(1)
    bot.edit_message_text("Iniciando 🟩🟩🟩🟩", message.chat.id, x.message_id)
    time.sleep(1)
    bot.edit_message_text("Bot iniciado, utiliza el comando /alta para generar aviso de disponibilidad de un producto, o utiliza el comando /aviso para comprobar tus avisos.", message.chat.id, x.message_id)
    hilo_scrap.start()

# Responde al comando /alta
@bot.message_handler(commands=["alta"])
def cmd_start(message):
    # Pregunta por la categoría a buscar
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Introduce el enlace del producto.", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_producto)


def preguntar_producto(message):
    # Se pregunta el producto deseado.
    if "https" not in message.text:
        markup = ForceReply()
        msg = bot.send_message(message.chat.id, "❌ Enlace no válido.")
        bot.register_next_step_handler(msg, preguntar_producto)
    else:
        producto = message.text
        bot.send_message(message.chat.id, "✅ Enlace correcto, aviso generado.")
        print(f'Producto elegido {producto}')
        producto_scrap = producto + "-reacondicionado"
        print(producto_scrap)
        markup = ReplyKeyboardMarkup(
            one_time_keyboard=True,
            input_field_placeholder="Pulsa un botón",
            resize_keyboard=True
            )
        markup.add("Seminuevo", "Reacondicionado")
        msg = bot.send_message(message.chat.id, "¿Que tipo de producto deseas?", reply_markup=markup)
        bot.register_next_step_handler(msg, guardar_datos_recibidos)


def guardar_datos_recibidos(message):
    # Guardamos los datos introducidos por el usuario.
    # Se comprueba si el botón pulsado es correcto.
    if message.text != "Seminuevo" and message.text != "Reacondicionado":
        # Se informa del error y se vuelve a preguntar.
        msg = bot.send_message(message.chat.id, "Elección no válida.\nPulsa un botón")
        # Se vuelve a ejecutar la función.
        bot.register_next_step_handler(msg, guardar_datos_recibidos)
        print(guardar_datos_recibidos)
    else:
        # Si la elección es válida.
        bot.send_message(message.chat.id, "Elección correcta")


# Responde a otros mensajes que no sean comandos
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    # Gestiona los mensajes de texto que recibe.
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Comando no disponible..")
    else:
        bot.send_message(message.chat.id, "No has enviado ningún comando..")


def scrap_pccom():
    options = uc.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
    driver = uc.Chrome(options=options)
    driver.maximize_window()
    driver.get('http://www.pccomponentes.com')


def scrap():
    scrap_pccom()

def recibir_mensajes():
    # Bucle infinito que comprueba si hay nuevos mensajes del bot.
    bot.infinity_polling()


# MAIL ###################################################
if __name__ == '__main__':
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Inicia el Bot."),
        telebot.types.BotCommand("/scrap", "Inicia la navegación."),
        telebot.types.BotCommand("/alta", "Inicia configuracion de la busqueda."),
        telebot.types.BotCommand("/avisos", "Detalle de avisos generados.")
    ])
    print('Iniciando el bot')
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_scrap = threading.Thread(name="hilo_scrap", target=scrap)
    hilo_bot.start()
    print("Bot iniciado")
