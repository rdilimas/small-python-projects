#instalar bibliotecas 
#pip install python-barcode
#pip instal pillow
#pip instal qrcode

from barcode import EAN13

#import para permitir salvar imagem como png
from barcode.writer import ImageWriter

import qrcode

#deve ser informado um padrão de 12 digitos
#codigo_barras = EAN13("123123123123", writer=ImageWriter())
#codigo_barras.save("codigo_barra")

codigos_produtos = {
    "Feijão": "551746511111",
    "Arroz": "665789011111",
    "Macarrao": "665887111111",
    "Azeite": "998556211111"
}

links_redes = {
    "LinkedIn": "https://www.linkedin.com/in/robson-lima-64990b68/",
    "Instagram": "https://www.instagram.com/robsondilima/",
    "GitHub": "https://github.com/rdilimas"
}

for produto in codigos_produtos:
    codigo_produto = (codigos_produtos[produto])
    codigo_barras = EAN13(codigo_produto, writer=ImageWriter())
    codigo_barras.save(f"codigo_barra_{produto}")

for link in links_redes:
    link_rede = (links_redes[link])
    imagem_qrcode = qrcode.make(link_rede)    
    imagem_qrcode.save(f"qrcode_python_{link}.png")
