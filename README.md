# ScrapNovel

**ScrapNovel** é uma aplicação web baseada em Streamlit para fazer scraping automatizado de web novels usando Selenium. O conteúdo extraído é tratado, limpo e compilado em um eBook `.docx`.

---

## 📈 Funcionalidades

### Módulo Web (Streamlit)

* Interface elegante e responsiva para entrada de dados.
* Inicia scraping com feedback visual e animações.
* Gera eBooks em `.docx` com títulos formatados.

### Scraper (core: `novel_scraper.py`)

* Navega entre capítulos via botão "próximo".
* Substitui expressões predefinidas (anti-spam/watermark).
* Remove censura por pontos ("s.e.x" → "sex").
* Gera log com ocorrências encontradas.

### Scripts Auxiliares

* `apaga_duplicados.py`: remove capítulos repetidos no `.docx` e gera log.
* `desfaz_censura.py`: remove censura por pontos.
* `limpa_docx.py`: aplica remoções e substituições com base no `pattern.py`.

---

## ⚙️ Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/RomanBrocki/ScrapStream.git

# Crie e ative o ambiente virtual (opcional)
python -m venv env
source env/bin/activate  # ou env\Scripts\activate no Windows

# Instale as dependências
pip install -r requirements.txt
```

---

## 🔧 Configuração do Scraper

Edite o arquivo `config.py` para definir:

```python
from selenium.webdriver.common.by import By

config = {
    'profile': r"caminho/para/perfil/chrome",
    'author': 'ScrapNovel',
    'chapter_title_selector': (By.CLASS_NAME, 'chr-text'),
    'chapter_content_selector': (By.ID, 'chr-content'),
    'next_chapter_selector': (By.ID, 'next_chap')
}
```

---

## 🚀 Executando a aplicação

```bash
streamlit run app.py
```

Acesse via navegador: [http://localhost:8501](http://localhost:8501)

---

## 🔮 Tutorial passo a passo

1. **Execute o app com Streamlit**:

   ```bash
   streamlit run app.py
   ```

2. **Abra o navegador** em `http://localhost:8501`

3. **Preencha os campos**:

   * Nome do eBook
   * URL do primeiro capítulo
   * URL do último capítulo
   * Caminho para salvar o arquivo `.docx`

4. **Clique em "Iniciar Scrap"**

   * Um GIF será exibido enquanto o scraping ocorre.
   * Ao final, uma mensagem de sucesso aparecerá com detalhes e o log.

---

## 📂 Estrutura de Arquivos

* `app.py`: Interface Streamlit
* `novel_scraper.py`: Lógica de scraping
* `config.py`: Configuração de seletores e perfil do navegador
* `pattern.py`: Lista de expressões a remover
* `desfaz_censura.py`: Remove censura com pontos
* `apaga_duplicados.py`: Remove capítulos duplicados
* `limpa_docx.py`: Aplica padrões de limpeza com `pattern`
* `assets/`: Imagens e GIFs para UI
* `requirements.txt`: Dependências

---

## 📊 Dependências

```txt
selenium
undetected_chromedriver
webdriver-manager(não recomendado)
python-docx
streamlit
```

---

## 🌐 Scripts Avulsos

Utilize diretamente via terminal para tratar arquivos `.docx` existentes:

```bash
python apaga_duplicados.py
python desfaz_censura.py
python limpa_docx.py
```

---

Projeto desenvolvido por Roman W. Brocki com foco em automação, praticidade e refinamento de eBooks gerados a partir de web novels.
