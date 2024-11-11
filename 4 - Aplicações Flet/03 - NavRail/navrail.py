from flet import *

def main(page:Page):

    page.title = "Usando NavRail"  

    rail = NavigationRail(
        selected_index=0,
        min_width=100,
        min_extended_width=200,
        label_type=NavigationRailLabelType.ALL,
        leading=FloatingActionButton(icon=icons.CREATE, text="Criar"),
        group_alignment=-0.9,
        destinations=[
            NavigationRailDestination(
                icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, label="Favoritos"
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.BOOKMARK_BORDER),
                selected_icon_content=Icon(icons.BOOKMARK),
                label="Marcar"
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,
                selected_icon=icons.SETTINGS,
                label="Configurações"
            )
        ],
        on_change = lambda e: print("Botão Clicado: ", e.control.selected_index)      
    )

    page.add(
        Row(
            [
                rail,
                VerticalDivider(width=1),
                Column([Text("Corpo da aplicação")], alignment==MainAxisAlignment.START, expand=True)
            ],     
            expand=True  
        )        
    ) 

app(target=main)