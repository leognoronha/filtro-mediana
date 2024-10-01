# Filtro de Mediana em Imagens PGM
## Engenharia da Computação 8º Semestre Fundação Santo André 
Leonardo Galis Noronha RA:741388 

## Descrição do Projeto

Este projeto aplica o filtro de mediana em imagens no formato PGM.

O programa permite que o usuário selecione uma imagem PGM de uma lista, aplica o filtro de mediana e gera uma comparação visual entre a imagem original e a imagem filtrada em uma página HTML.

## Fluxo do Programa

1. **Inicialização**:
   - O programa começa exibindo uma lista de imagens disponíveis na pasta `imagens/imagem_original/`.
   - O usuário é solicitado a escolher uma imagem para aplicar o filtro.

2. **Processamento da Imagem**:
   - A imagem selecionada é carregada e convertida para um array NumPy.
   - O filtro de mediana é aplicado utilizando um kernel de tamanho definido (padrão é 3).
   - A imagem original é salva em formato PNG para visualização.
   - A imagem filtrada é salva em dois formatos:
     - **PGM (ASCII)**: Mantém o formato original, permitindo análises adicionais.
     - **PNG**: Facilita a visualização em navegadores e editores de imagens.

3. **Criação da Página HTML**:
   - Uma página HTML é gerada, exibindo a imagem original e a filtrada lado a lado.
   - Esta página permite uma comparação visual direta entre as duas imagens.

4. **Organização dos Resultados**:
   - Todos os arquivos gerados (imagem original PNG, imagem filtrada PGM e PNG, página HTML) são salvos em uma pasta específica dentro de `imagens/imagem_filtrada/`, nomeada com base na imagem original (por exemplo, `cameraman_files/`).

## Bibliotecas Utilizadas

O projeto utiliza as seguintes bibliotecas:

1. **NumPy** (`numpy`):
   - **Descrição**: Biblioteca fundamental para computação numérica em Python, proporcionando suporte para arrays e matrizes multidimensionais, além de uma grande coleção de funções matemáticas de alto nível.
   - **Uso no Projeto**:
     - Manipulação de arrays de pixels da imagem.
     - Conversão entre formatos de dados para processamento eficiente.

2. **Pillow** (`PIL`):
   - **Descrição**: Biblioteca de processamento de imagens amigável ao usuário, sendo uma continuação da PIL (Python Imaging Library). Suporta diversos formatos de imagem e fornece funcionalidades para abrir, manipular e salvar imagens.
   - **Uso no Projeto**:
     - Carregamento e conversão das imagens PGM.
     - Salvamento das imagens em formatos PGM e PNG.
     - Conversão entre objetos de imagem e arrays NumPy.

3. **SciPy** (`scipy`):
   - **Descrição**: Biblioteca que oferece algoritmos e ferramentas matemáticas avançadas para Python, incluindo otimização, integração, interpolação, álgebra linear, estatística e processamento de sinais e imagens.
   - **Uso no Projeto**:
     - Aplicação do filtro de mediana através da função `median_filter` presente em `scipy.ndimage`.
     - O `median_filter` é eficiente para reduzir ruídos em imagens, substituindo cada pixel pela mediana dos pixels vizinhos definidos pelo tamanho do kernel.

4. **OS** (`os`):
   - **Descrição**: Módulo padrão do Python que fornece uma maneira portátil de usar funcionalidades dependentes do sistema operacional.
   - **Uso no Projeto**:
     - Manipulação de caminhos de arquivos e diretórios.
     - Verificação e criação de pastas necessárias.
     - Listagem de arquivos em diretórios.

## Descrição dos Arquivos

### 1. `filtro_mediana.py`

Este é o script principal que coordena a execução do programa.

**Responsabilidades**:
- Exibir as imagens disponíveis para o usuário e solicitar a seleção.
- Definir caminhos e nomes de arquivos para salvar os resultados.
- Chamar as funções de processamento e criação de HTML.
- Organizar os arquivos gerados em pastas específicas.
- Exibir mensagens informativas sobre o progresso e a conclusão das tarefas.

### 2. `processamento/imagem.py`

Contém funções relacionadas ao processamento de imagens.

**Função Principal**:

- `aplicar_filtro_mediana(...)`:
  - **Descrição**: Aplica o filtro de mediana à imagem selecionada.
  - **Processos**:
    - Carrega a imagem original e converte para escala de cinza.
    - Converte a imagem para um array NumPy para processamento.
    - Aplica o filtro de mediana utilizando o tamanho de kernel especificado.
    - Salva a imagem original em PNG.
    - Salva a imagem filtrada em PGM (ASCII) e PNG.
    - Exibe mensagens de status.

### 3. `processamento/utils.py`

Contém funções utilitárias usadas pelo programa.

**Funções**:

- `salvar_pgm_ascii(caminho_arquivo, array)`:
  - **Descrição**: Salva um array NumPy como uma imagem PGM no formato P2 (ASCII).
  - **Processos**:
    - Escreve o cabeçalho do arquivo PGM.
    - Escreve os valores dos pixels em formato ASCII.

- `criar_pagina_html(nome_imagem_original_png, nome_imagem_filtrada_png, caminho_html)`:
  - **Descrição**: Cria uma página HTML que exibe a imagem original e a imagem filtrada lado a lado.
  - **Processos**:
    - Gera o conteúdo HTML com estrutura e estilos básicos.
    - Insere as imagens usando os nomes dos arquivos PNG fornecidos.
    - Salva o arquivo HTML no caminho especificado.


## Como Executar o Programa

### 1. Pré-requisitos

- **Python 3.x** instalado no sistema.
- Instalar as bibliotecas necessárias listadas em `requirements.txt`.

### 2. Instalação das Dependências

No terminal, navegue até o diretório raiz do projeto e execute:
```bash
pip install -r requirements.txt
```

### 3. Preparação das Imagens

Coloque as imagens que deseja processar no formato PGM (P2 - ASCII) dentro da pasta:
 ```bash
imagens/imagem_original/`
```
Certifique-se de que as imagens estão corretamente formatadas.

### 4. Executando o Programa

No terminal, a partir do diretório raiz do projeto, execute:
```bash
python filtro_mediana.py
```
### 5. Interação com o Programa

-   **Seleção da Imagem**: O programa exibirá uma lista numerada das imagens disponíveis. Digite o número correspondente à imagem que deseja filtrar e pressione **Enter**.
-   **Processamento**: O programa aplicará o filtro de mediana e informará sobre o progresso.
-   **Resultados**:
    -   Os arquivos gerados serão salvos em uma nova pasta dentro de `imagens/imagem_filtrada/`, nomeada com o padrão `[nome_da_imagem]_files`.
    -   Exemplo: Se a imagem selecionada for `cameraman.pgm`, os resultados estarão em `imagens/imagem_filtrada/cameraman_files/`.

    ### 6. Visualizando os Resultados

-   Abra o arquivo HTML gerado (`[nome_da_imagem]_comparacao.html`) no seu navegador para visualizar a comparação entre a imagem original e a filtrada.
-   As imagens em formato PNG também podem ser visualizadas individualmente em qualquer visualizador de imagens.

## Detalhes Adicionais

### Tamanho do Kernel

-   O tamanho do kernel utilizado no filtro de mediana é definido pela variável `tamanho_kernel` no script `filtro_mediana.py`.
-   Por padrão, está definido como `3`, mas pode ser ajustado conforme necessário.
-   **Observação**: O tamanho do kernel deve ser um número ímpar positivo.