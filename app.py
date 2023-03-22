import os
import smtplib
from email.message import EmailMessage

# Configurar email, senha

EMAIL_ADRESS = ''    # Email
EMAIL_PASSWORD = ''  # Senha do email

# Criando a mensagem

msg = EmailMessage()
msg['Subject'] = 'Carga chegou ao porto'
msg['From'] = ''  # Quem está enviando o email
msg['To'] = ''    # Quem está recebendo

msg.set_content('Favor buscar a carga que acabou de chegar na portaria')

# Enviando o email

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    
    # Devido as novas politicas do Google, é preciso gerar uma senha para apps terceiros.
