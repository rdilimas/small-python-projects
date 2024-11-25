import flet as ft

def main(page: ft.Page):

    def botao_clicado(e):
        textoColorido.value = f"Cor selecionado no Dropdown :  {dropdown.value}"
        if  dropdown.value  == "Vermelho":
            textoColorido.color='Red'
        elif dropdown.value == 'Verde':
            textoColorido.color='Green'
        elif dropdown.value == 'Azul':  
            textoColorido.color='Blue'    
        else:  
            textoColorido.color='Black'       
        page.update()   

    textoColorido = ft.Text()
    btn_selecionar = ft.ElevatedButton(text="Selecionar cor", on_click=botao_clicado)
    dropdown = ft.Dropdown(
        width=200,
        options=[
            ft.dropdown.Option("Vermelho"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Nenhuma"),
        ],
    )
    page.add(dropdown, btn_selecionar, textoColorido)

ft.app(main)