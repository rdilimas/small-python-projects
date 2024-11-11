from flet import *

def main(page:Page):

    page.appbar = AppBar(
        leading=Icon(icons.CODE),
        bgcolor="#008B8B",
        #leading_width=40,
        title=Text("Titulo da página"),
        center_title=True,
        color="#DCDCDC", 
        actions=[
            IconButton(icons.WB_SUNNY_OUTLINED),
            PopupMenuButton(
                items=[
                    PopupMenuItem("Logar"),
                    PopupMenuItem(),
                    PopupMenuItem("Sair")
                ]
            )
        ]
    )

    page.add(
        Text("Corpo da aplicação")            
        ) 

app(target=main)