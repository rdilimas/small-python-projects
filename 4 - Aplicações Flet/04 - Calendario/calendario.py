from flet import *
import datetime

def main(page:Page):

    cor_botoes = "#87CEFA"
    #page.window.width  = 420
    #page.window.height = 520
    page.theme_mode = ThemeMode.LIGHT
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment   = MainAxisAlignment.CENTER

    #atualizar o recv_data com a data selecionada no calendário
    def set_data_text(e):
        recv_data.value = f"{e.control.value.strftime('%d/%m/%Y')}"
        recv_data.update()

    #caso abra o calendario e feche sem selecionar data
    def valor_nao_select(e):
        #caso esteja vazio dispara a mensagem
        if recv_data.value == "":
           recv_data.value = 'Selecione uma data'
           recv_data.update()

    calendario = DatePicker(
        first_date= datetime.datetime(year=1980, month=1, day=1),

        #Limitar data maxima selecionada a data corrente
        last_date = datetime.datetime.now(),      
        on_change=set_data_text,
        on_dismiss=valor_nao_select     
    ) 
    print(datetime.datetime(year=2024, month=11, day=17),)
    dtatual = datetime.datetime.now() 
    print(dtatual)

    recv_data = TextField(
        width=200,
        border=2,
        color= colors.BLACK,
        label="Selecionar Data"
    )

    abrir_calendario = ElevatedButton(
        text="Selecionar Data",
        icon=icons.CALENDAR_MONTH,
        bgcolor=cor_botoes,
        color=colors.BLACK,
        on_click= lambda e: page.open(calendario)
    )

    def botao_clean_clicado(e):
        recv_data.value = ""
        recv_data.update()
        
    btn_icone = ElevatedButton(
            width=150,
            content=Row(
                [
                    IconButton(
                        icon=icons.CALENDAR_MONTH,
                        icon_color=colors.BLACK,
                        icon_size=25,
                        tooltip="Selecionar Data",
                        on_click= lambda e: page.open(calendario)
                    ),
                    IconButton(
                        icon=icons.CLEANING_SERVICES,
                        icon_color=colors.BLACK,
                        icon_size=25,
                        tooltip="Limpar Data",
                        on_click=botao_clean_clicado
                    )
                    
                ],
                alignment=MainAxisAlignment.SPACE_AROUND,
            ),  
            bgcolor=cor_botoes,    
        )

    page.add(
        #adicionado uma Row, para que os componentes ficassem na mesma linha
        Row(
                [
                    recv_data, abrir_calendario, btn_icone
                ],
                alignment=MainAxisAlignment.CENTER
            )
    ) 

app(target=main)
