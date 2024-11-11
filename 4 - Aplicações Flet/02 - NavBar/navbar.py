from flet import *

def main(page:Page):

    page.title = "Usando NavBar"  

    page.navigation_bar = NavigationBar(
        destinations=[
            NavigationBarDestination(icon=icons.HOME, label="Home"),
            NavigationBarDestination(icon=icons.CONTACTS, label="Contatos"),
            NavigationBarDestination(icon=icons.CHAT, label="Mensagem")
        ]
    )

    page.add(
        Text("Corpo da aplicação")            
        ) 

app(target=main)