import flet as ft

def main(page: ft.Page):

    page.title = "Trabalhando com Temas"   

    #opção 1 - Validando pelo e.data
    def alterando_tema(e):
        
        if e.data == "true":
            page.theme_mode = ft.ThemeMode.DARK
            print("DARK")
        else:  
            page.theme_mode = ft.ThemeMode.LIGHT
            print("LIGHT")
        page.update()

    #opção 2 - Usando page.theme_mode
    def alterando_tema_2(e):
        if page.theme_mode == ft.ThemeMode.DARK:
           page.theme_mode = ft.ThemeMode.LIGHT 
           switch.label = "Alterar o Tema para Escuro"
        else:
           page.theme_mode = ft.ThemeMode.DARK
           switch.label = "Alterar o Tema para Claro"
        page.update()

    
    switch = ft.Switch(label="Clique aqui para selecionar o tema", on_change=alterando_tema)

    page.add(switch)

ft.app(target=main)