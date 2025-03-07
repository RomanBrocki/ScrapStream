# ScrapNovel

ScrapNovel é uma aplicação web baseada em Streamlit, projetada para fazer scraping de web novels utilizando Selenium e compilar o conteúdo extraído em formatos de eBook estruturados.

## Funcionalidades

- **Scraping de Web Novels**: Automatiza a extração de conteúdo de web novels.
- **Interface Interativa**: Fornece uma interface fácil de usar para inserir os detalhes da novel e iniciar o processo de scraping.
- **Compilação de eBooks**: Compila o conteúdo extraído em formatos de eBook estruturados.
- **Configuração Personalizável**: Agora com o arquivo `config.py`, você pode personalizar facilmente os seletores, o autor do eBook e a configuração do perfil do navegador para cada web novel.

## Instalação

1. **Clone o repositório**:

    
    git clone https://github.com/RomanBrocki/ScrapStream.git
   
    

3. **Configure um ambiente virtual (opcional, mas recomendado)**:

    
    python -m venv env
   
    source env/bin/activate  # No Windows: env\Scripts\activate
    

4. **Instale as dependências necessárias**:

   
    pip install -r requirements.txt


5. **Configure o arquivo `config.py`**:

   O arquivo `config.py` permite que você defina os **seletores dos elementos HTML**, o **caminho do perfil do Chrome** e o **autor do eBook**.
   Certifique-se de que os valores em `config.py` estão corretos de acordo com suas preferências e com as web novels que você está fazendo scraping.

   Exemplo de `config.py`:

   
   from selenium.webdriver.common.by import By

   config = {
       'profile': r"c:\Users\Roman\AppData\Local\Google\Chrome\User Data\Profile Selenium",  # Caminho do perfil do Chrome

       'author': 'ScrapNovel',  # Autor do eBook

       'chapter_title_selector': (By.CLASS_NAME, 'chr-text'),  # Seletor para título do capítulo

       'chapter_content_selector': (By.ID, 'chr-content'),  # Seletor para conteúdo do capítulo

       'next_chapter_selector': (By.ID, 'next_chap')  # Seletor do botão de próximo capítulo
   }
   

## Uso

1. **Execute o aplicativo Streamlit**:

    
    streamlit run app.py
    

2. **Acesse a aplicação**:

    Abra seu navegador e acesse o endereço:

    
    http://localhost:8501
    

3. **Forneça as informações necessárias**:

    - **Nome do Ebook**: Insira o nome desejado para o seu eBook.
    - **URL do primeiro capítulo**: Forneça a URL do primeiro capítulo da novel.
    - **URL do último capítulo**: Forneça a URL do último capítulo da novel.
    - **Caminho para salvar o ebook**: Especifique o diretório onde o eBook será salvo.

4. **Inicie o processo de scraping**:

    Clique no botão "Iniciar Scrap" para começar o scraping e compilar o eBook.
    Possivelmente sistemas antiscrap como cloudflare podem pedir check anti robô. Você pode fazer o check manualmente ou aguardar que o código (e scrap) seguirá após um tempo.

## Estrutura de Arquivos:

- **app.py**: Arquivo principal da aplicação Streamlit.

- **novel_scraper.py**: Contém a classe `NovelScraper`, responsável pela lógica de scraping.

- **config.py**: Arquivo de configuração para personalizar os seletores, o autor e o perfil do navegador.

- **assets/**: Diretório contendo recursos estáticos como imagens de fundo e GIFs.

- **requirements.txt**: Lista de dependências Python necessárias para o projeto.

- **pattern.py**: Arquivo legado com medidas anti-scraping e textos watermark.

## Dependências:

- **Streamlit**: Para construir a interface web.

- **Selenium**: Para automatizar a interação com o navegador e realizar o scraping de conteúdo.

- **python-docx**: Para criar arquivos `.docx` a partir do conteúdo extraído.

- **webdriver-manager**: Para gerenciar automaticamente o ChromeDriver utilizado pelo Selenium.

- **Configurações customizáveis**: A aplicação agora usa o `config.py` para tornar a personalização dos seletores, perfil de navegador e autor mais fácil e flexível.

- **pattern**: Para exclusão de textos watermark e outros padrões no conteúdo.

Todas as dependências estão listadas no arquivo `requirements.txt`.
