import flet as ft

def main(page):
    def button_clicked(e):
        t.value = (
            f"Checkboxes values are:  {c1.value}, {c2.value}, {c3.value}, {c4.value}, {c5.value}."
        )
        page.update()

    t = ft.Text()
    #Default false
    c1 = ft.Checkbox(label="Unchecked by default checkbox", value=False)
    #Default None, com possibilidade de True o False
    c2 = ft.Checkbox(label="Undefined by default tristate checkbox", tristate=True)
    #Default True
    c3 = ft.Checkbox(label="Checked by default checkbox", value=True)
    #Bloqueado para seleção
    c4 = ft.Checkbox(label="Disabled checkbox", disabled=True)
    #checkBox orientado a direita do texto 
    c5 = ft.Checkbox(
        label="Checkbox with rendered label_position='left'", label_position=ft.LabelPosition.LEFT
    )
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(c1, c2, c3, c4, c5, b, t)

ft.app(main)