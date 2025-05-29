# 📚 ScrapNovel

**ScrapNovel** é uma aplicação web baseada em **Streamlit** para scraping automatizado de web novels. Utiliza **Selenium com `undetected_chromedriver`** para contornar bloqueios como Cloudflare e compila os capítulos extraídos em um eBook `.docx` limpo e legível.

---

## 📊 Funcionalidades

### 🔹 Módulo Web (`app.py`)

* Interface responsiva com Streamlit
* Entrada intuitiva dos dados (nome do eBook, URLs, saída)
* Feedback visual com animação de progresso
* Geração automatizada de `.docx` com estrutura e títulos formatados

### 🔹 Núcleo do Scraper (`novel_scraper.py`)

* Todas as operações centralizadas em uma **classe `NovelScraper`**
* Navegação automática capítulo a capítulo via botão "Próximo"
* Substituições personalizadas com base em `pattern.py`
* Remove censura por pontos (ex.: `s.e.x` → `sex`)
* Gera log detalhado com expressões tratadas
* **Função `scrape_chapters()` adaptada para contornar o Cloudflare**, com lógica de retry, espera e scrolldown

### 🔹 Scripts Auxiliares

* `apaga_duplicados.py`: remove capítulos repetidos no `.docx`
* `desfaz_censura.py`: limpa censura por pontos em arquivos existentes
* `limpa_docx.py`: aplica as substituições definidas em `pattern.py`

---

## ⚙️ Instalação

```bash
# Clone o repositório
git clone https://github.com/RomanBrocki/ScrapStream.git

# Crie e ative o ambiente virtual (opcional)
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

---

## 🛠️ Configuração

Edite o arquivo `config.py` para definir o perfil do Chrome e os seletores CSS/ID usados nos capítulos:

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

## 🚀 Como Executar

```bash
streamlit run app.py
```

Abra no navegador: [http://localhost:8501](http://localhost:8501)

---

## 📋 Tutorial Rápido

1. Execute o app com `streamlit run app.py`
2. Preencha:

   * Nome do eBook
   * URL do primeiro capítulo
   * URL do último capítulo
   * Caminho para salvar o `.docx`
3. Clique em **"Iniciar Scrap"**
4. Acompanhe o progresso via animação (GIF)
5. Ao final, uma mensagem de sucesso será exibida com o log salvo

---

## 📂 Estrutura do Projeto

| Arquivo/Pasta         | Descrição                                            |
| --------------------- | ---------------------------------------------------- |
| `app.py`              | Interface em Streamlit                               |
| `novel_scraper.py`    | Lógica de scraping (classe `NovelScraper`)           |
| `config.py`           | Configurações de scraping e perfil do Chrome         |
| `pattern.py`          | Expressões e palavras a serem removidas/substituídas |
| `desfaz_censura.py`   | Remove censura por pontos                            |
| `apaga_duplicados.py` | Elimina capítulos repetidos                          |
| `limpa_docx.py`       | Aplica padrão de limpeza em `.docx`                  |
| `assets/`             | Imagens e animações para interface                   |
| `requirements.txt`    | Lista de dependências do projeto                     |

---

## 📦 Dependências

* `selenium`
* `undetected-chromedriver`
* `streamlit`
* `python-docx`

> ⚠️ `webdriver-manager` está incluído, mas **não recomendado**, pois não contorna bloqueios como o Cloudflare.

---

## 🧹 Scripts Avulsos

Execute no terminal para tratar `.docx` existentes:

```bash
python apaga_duplicados.py
python desfaz_censura.py
python limpa_docx.py
```

---

## 👨‍💻 Autor

Desenvolvido por **Roman W. Brocki**, com foco em automação, praticidade e refinamento textual para eBooks extraídos de web novels.

---

