import os
from processamento.imagem import aplicar_filtro_mediana
from processamento.utils import criar_pagina_html

if __name__ == "__main__":
    # Define as pastas
    pasta_imagens_originais = 'imagens/imagem_original'   # Pasta com imagens originais
    pasta_imagens_filtradas = 'imagens/imagem_filtrada'   # Pasta para salvar imagens filtradas

    # Garante que a pasta de saída existe
    if not os.path.exists(pasta_imagens_filtradas):
        os.makedirs(pasta_imagens_filtradas)

    # Tamanho do kernel (deve ser um número ímpar positivo)
    tamanho_kernel = 3

    # Lista os arquivos na pasta de imagens originais
    arquivos_imagem = [f for f in os.listdir(pasta_imagens_originais) if f.endswith('.pgm')]

    # Verifica se há imagens na pasta
    if not arquivos_imagem:
        print("Nenhuma imagem encontrada na pasta imagens/imagem_original.")
        exit()

    # Exibe a lista de imagens disponíveis
    print("Escolha uma imagem que deseja filtrar:")
    for idx, nome_arquivo in enumerate(arquivos_imagem, start=1):
        print(f"{idx}. {nome_arquivo}")

    # Solicita ao usuário que selecione uma imagem
    while True:
        try:
            opcao = int(input("Digite o número da imagem escolhida: "))
            if 1 <= opcao <= len(arquivos_imagem):
                nome_imagem_entrada = arquivos_imagem[opcao - 1]
                break
            else:
                print("Opção inválida. Por favor, escolha um número da lista.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    # Caminho completo para o arquivo de entrada
    caminho_imagem_entrada = os.path.join(pasta_imagens_originais, nome_imagem_entrada)

    # Extrai o nome base e extensão
    nome_base, extensao = os.path.splitext(nome_imagem_entrada)
    nome_base = os.path.basename(nome_base)  # Garante que apenas o nome do arquivo seja usado

    # Nome da pasta específica para a imagem (ex: 'cameraman_files')
    nome_pasta_imagem = f"{nome_base}_files"

    # Caminho completo para a nova pasta dentro de 'imagem_filtrada'
    caminho_pasta_imagem = os.path.join(pasta_imagens_filtradas, nome_pasta_imagem)

    # Garante que a pasta da imagem existe
    if not os.path.exists(caminho_pasta_imagem):
        os.makedirs(caminho_pasta_imagem)

    # Nomes dos arquivos de saída
    nome_imagem_saida_pgm = f"{nome_base}_filtrado{extensao}"
    nome_imagem_saida_png = f"{nome_base}_filtrado.png"
    nome_imagem_original_png = f"{nome_base}_original.png"

    # Caminhos completos para os arquivos de saída
    caminho_imagem_saida_pgm = os.path.join(caminho_pasta_imagem, nome_imagem_saida_pgm)
    caminho_imagem_saida_png = os.path.join(caminho_pasta_imagem, nome_imagem_saida_png)
    caminho_imagem_original_png = os.path.join(caminho_pasta_imagem, nome_imagem_original_png)

    # Aplica o filtro de mediana
    aplicar_filtro_mediana(
        caminho_imagem_entrada,
        caminho_imagem_saida_pgm,
        caminho_imagem_saida_png,
        caminho_imagem_original_png,
        tamanho_kernel
    )

    # Caminho para salvar a página HTML
    caminho_pagina_html = os.path.join(caminho_pasta_imagem, f"{nome_base}_comparacao.html")

    # Cria a página HTML
    criar_pagina_html(nome_imagem_original_png, nome_imagem_saida_png, caminho_pagina_html)

    print(f"Página HTML criada em {caminho_pagina_html}")
