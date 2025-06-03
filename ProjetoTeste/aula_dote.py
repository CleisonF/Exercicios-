from dotenv import load_dotenv
import os


load_dotenv()
#sempre crie o .env-example e nunca envie seu proprio env para o repositorio
# Dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# Configurações SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')