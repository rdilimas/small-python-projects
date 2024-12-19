from flet import *
from twilio.rest import Client
import os
from dotenv import load_dotenv

def main(page:Page):

    def botao_clean_clicado(e):
        numero.value = "Digite o número celular"
        mensagem_digitada.value = "Digite a mensagem a ser enviada"
        numero.update()
        mensagem_digitada.update()
        print("Clean clicado")

    page.appbar = AppBar(
        leading=Icon(icons.CODE),
        bgcolor="#008B8B",
        #leading_width=40,
        title=Text("Envio de SMS - Com Twillio"),
        center_title=True,
        color="#DCDCDC", 
        actions=[
            IconButton(icons.CLEANING_SERVICES,
                       on_click=botao_clean_clicado),
        ]
    )

    def enviar(e):

        print("Enviado!!!", e)
        load_dotenv()
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        cliente = Client(account_sid, auth_token)

        mensagem = cliente.messages.create(
            from_= os.environ["FROM_"],
            to=numero.value,
            body=mensagem_digitada.value
        )    

    txt_numero = Text('Número celular:')
    numero = TextField(label="Digite o número celular", text_align=TextAlign.LEFT)    
    txt_msg = Text('Mensagem a ser enviada:')
    mensagem_digitada = TextField(label="Digite a mensagem a ser enviada:", text_align=TextAlign.LEFT)     
    btn_enviar = ElevatedButton("Enviar", on_click=enviar, icon=icons.SEND)

    page.add(
        txt_numero,
        numero,
        txt_msg,
        mensagem_digitada,
        btn_enviar      
        ) 

app(target=main)