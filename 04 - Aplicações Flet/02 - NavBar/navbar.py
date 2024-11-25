from flet import *

def main(page:Page):

    chamadasPerdidas = "5"

    page.title = "Usando NavBar"  

    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationBarDestination(icon=icons.HOME, label="Home"),
            NavigationBarDestination(icon=icons.CONTACTS, label="Contatos"),
            NavigationBarDestination(icon=icons.CHAT, label="Mensagem"),
            #icon_content para adicionar informação de notificações na aplicação, ex: chamadas perdidas e mensagen...
            NavigationBarDestination(icon_content=Badge(content=Icon(icons.PHONE), text=chamadasPerdidas), label="Telefone")
        ]
    )

    page.add(
        Text("Corpo da aplicação")            
        ) 

app(target=main)