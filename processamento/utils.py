def salvar_pgm_ascii(caminho_arquivo, array):
    """
    Salva um array NumPy como uma imagem PGM no formato P2 (ASCII).
    """
    with open(caminho_arquivo, 'w') as f:
        # Escreve o cabeçalho do arquivo PGM
        f.write('P2\n')
        f.write(f'{array.shape[1]} {array.shape[0]}\n')  # Largura e altura
        f.write('255\n')  # Valor máximo de intensidade de pixel

        # Escreve os valores dos pixels
        for row in array:
            linha = ' '.join(str(int(pixel)) for pixel in row)
            f.write(linha + '\n')

def criar_pagina_html(nome_imagem_original_png, nome_imagem_filtrada_png, caminho_html):
    """
    Cria uma página HTML que exibe a imagem original e a imagem filtrada lado a lado.

    Parâmetros:
    - nome_imagem_original_png: str, nome do arquivo PNG da imagem original.
    - nome_imagem_filtrada_png: str, nome do arquivo PNG da imagem filtrada.
    - caminho_html: str, caminho para salvar o arquivo HTML.
    """
    html_conteudo = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Comparação de Imagens</title>
    <style>
        .container {{
            display: flex;
            flex-direction: row;
        }}
        .imagem {{
            margin: 10px;
            text-align: center;
        }}
        img {{
            max-width: 100%;
            height: auto;
        }}
    </style>
</head>
<body>
    <h1>Imagem Original vs Imagem Filtrada</h1>
    <div class="container">
        <div class="imagem">
            <h2>Imagem Original</h2>
            <img src="{nome_imagem_original_png}" alt="Imagem Original">
        </div>
        <div class="imagem">
            <h2>Imagem Filtrada</h2>
            <img src="{nome_imagem_filtrada_png}" alt="Imagem Filtrada">
        </div>
    </div>
</body>
</html>
"""
    with open(caminho_html, 'w', encoding='utf-8') as f:
        f.write(html_conteudo)
