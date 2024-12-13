
'''Nessa dica vou explicar como habilitar o suporte a caminhos longos no Windows 10. 

   Isso vai permitir que você crie arquivos e pastas que tenham caminhos com mais de 260 caracteres:
   Pelo Registro do Windows:

   Pressione as teclas WINDOWS + R para abrir o comando Executar e digite o seguinte comando: regedit e pressione ENTER 
   Dentro do registro do Windows siga até o seguinte local:
   HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem\
   Dentro de FileSystem localize o valor LongPathsEnabled, clique duas vezes sobre ele e defina seu valor igual a 1
'''

from twilio.rest import Client

#interface com o sistema operacional 
import os
from dotenv import load_dotenv

#Carregar arquivo .env
load_dotenv()

#accountid do twilio
account_sid = os.environ["TWILIO_ACCOUNT_SID"]

#auth_token do twilio
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

cliente = Client(account_sid, auth_token)

mensagem = cliente.messages.create(
    #de onde vai ser enviado, informação do twilio
    from_= os.environ["FROM_"],
    #para onde vai ser enviado, pode ser pessoal ou twilio
    to=os.environ["TO"],
    #mensagem a ser enviada. 
    body="Testando Envio de SMS Twilio"
)

resposta = mensagem.status
sid      = mensagem.sid

print(resposta)
print(sid)
