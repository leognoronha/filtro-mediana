import numpy as np
from PIL import Image
from scipy.ndimage import median_filter
from .utils import salvar_pgm_ascii

def aplicar_filtro_mediana(nome_arquivo_entrada, nome_arquivo_saida_pgm, nome_arquivo_saida_png, nome_arquivo_original_png, tamanho_kernel):
    """
    Aplica o filtro de mediana em uma imagem PGM e salva em PGM e PNG.

    Parâmetros:
    - nome_arquivo_entrada: str, caminho para a imagem de entrada.
    - nome_arquivo_saida_pgm: str, caminho para salvar o arquivo PGM filtrado.
    - nome_arquivo_saida_png: str, caminho para salvar o arquivo PNG filtrado.
    - nome_arquivo_original_png: str, caminho para salvar a imagem original em PNG.
    - tamanho_kernel: int, tamanho do kernel (deve ser um número ímpar).
    """
    try:
        # Carrega a imagem em modo grayscale ('L' de luminosidade)
        imagem = Image.open(nome_arquivo_entrada).convert('L')

        # Converte a imagem PIL em um array NumPy
        imagem_array = np.array(imagem)

        # Salva a imagem original em PNG
        imagem.save(nome_arquivo_original_png)

        # Exibe mensagem de processamento
        print("\nProcessando imagem...")

        # Aplica o filtro de mediana com o tamanho de kernel especificado
        imagem_filtrada = median_filter(imagem_array, size=tamanho_kernel)

        # Salva a imagem filtrada em formato P2 (ASCII)
        salvar_pgm_ascii(nome_arquivo_saida_pgm, imagem_filtrada)

        # Salva a imagem filtrada em formato PNG
        imagem_png = Image.fromarray(imagem_filtrada.astype(np.uint8))
        imagem_png.save(nome_arquivo_saida_png)

        # Exibe mensagem de sucesso
        print("Imagem filtrada com sucesso!")
        print(f"Imagem PGM filtrada salva como {nome_arquivo_saida_pgm}")
        print(f"Imagem PNG filtrada salva como {nome_arquivo_saida_png}")
        print(f"Imagem original PNG salva como {nome_arquivo_original_png}")

    except FileNotFoundError:
        print(f"Erro: Arquivo {nome_arquivo_entrada} não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
