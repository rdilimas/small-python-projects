import flet as ft
from models import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///projeto2.db"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
session = Session()

def main(page: ft.Page):
    page.title = "Cadastro App"

    lista_produtos = ft.ListView()
    def cadastrar(e):
        try:
            novo_produto = Produto(titulo=produto.value, preco=preco.value)
            session.add(novo_produto)
            session.commit()
            print("Produto cadastrado com Sucesso!")
            lista_produtos.controls.append(ft.Container(
                    ft.Text(produto.value),
                    bgcolor=ft.colors.BLACK12,
                    padding=15,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=10
                ))
            txt_erro.visible = False
            txt_ok.visible = True
        except:
            txt_erro.visible = True
            txt_ok.visible = False    
        page.update()

    txt_erro = ft.Container(ft.Text('Erro ao Salvar produto'), visible=False, 
                                                               bgcolor=ft.colors.RED, 
                                                               padding=10, 
                                                               alignment=ft.alignment.center, 
                                                               border_radius=10)
    txt_ok   = ft.Container(ft.Text('Produto Cadastrado com Sucesso!'), visible=False, 
                                                                        bgcolor=ft.colors.GREEN, 
                                                                        padding=10, 
                                                                        alignment=ft.alignment.center, 
                                                                        border_radius=10)

    txt_titulo = ft.Text('Titulo do Produto:')
    produto = ft.TextField(label="Digite o Titulo do Produto", text_align=ft.TextAlign.LEFT)    
    txt_preço = ft.Text('Preço do Produto:')
    preco = ft.TextField(value=0, label="Digite o Preço do Produto", text_align=ft.TextAlign.LEFT)     
    btn_produto = ft.ElevatedButton("Cadastrar", on_click=cadastrar)
    page.add(
          txt_ok
         ,txt_erro
         ,txt_titulo
         ,produto
         ,txt_preço
         ,preco
         ,btn_produto
     )
    
    for p in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(p.titulo),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
            )
            
            )

    page.add(
          lista_produtos
     )
ft.app(target=main)