ScrapStream
ScrapStream é uma aplicação web baseada em Streamlit, projetada para fazer scraping de web novels utilizando Selenium e compilar o conteúdo extraído em formatos de eBook estruturados.

Funcionalidades

Scraping de Web Novels: Automatiza a extração de conteúdo de web novels.

Interface Interativa: Fornece uma interface fácil de usar para inserir os detalhes da novel e iniciar o processo de scraping.

Compilação de eBooks: Compila o conteúdo extraído em formatos de eBook estruturados.

Instalação

1. Clone o repositório:

  git clone https://github.com/RomanBrocki/ScrapStream.git

  cd ScrapStream

2. Configure um ambiente virtual (opcional, mas recomendado):

  python -m venv env

  source env/bin/activate  # On Windows: env\Scripts\activate

3. Instale as dependências necessárias:

  pip install -r requirements.txt

Uso

1. Execute o aplicativo Streamlit:

  streamlit run app.py

2. Acesse a aplicação:

Abra seu navegador e acesse o endereço:

  http://localhost:8501

3. Forneça as informações necessárias:

Nome do Ebook: Insira o nome desejado para o seu eBook.

URL do primeiro capítulo: Forneça a URL do primeiro capítulo da novel.

URL do último capítulo: Forneça a URL do último capítulo da novel.

Caminho para salvar o ebook: Especifique o diretório onde o eBook será salvo.

4. Inicie o processo de scraping:

Clique no botão "Iniciar Scrap" para começar o scraping e compilar o eBook.

Estrutura de Arquivos:

app.py: Arquivo principal da aplicação Streamlit.
novel_scraper.py: Contém a classe NovelScraper, responsável pela lógica de scraping.
assets/: Diretório contendo recursos estáticos como imagens de fundo e GIFs.
requirements.txt: Lista de dependências Python necessárias para o projeto.
pattern.py : arquivo legado para medidas antiscraping co textos watermark

Dependências:

Streamlit: Para construir a interface web.
Selenium: Para automatizar a interação com o navegador e realizar o scraping de conteúdo.
python-docx: Para criar arquivos .docx a partir do conteúdo extraído.
webdriver-manager: Para gerenciar automaticamente o ChromeDriver utilizado pelo Selenium.
Todas as dependências estão listadas no arquivo requirements.txt.
