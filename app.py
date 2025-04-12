import streamlit as st
import streamlit.components.v1 as components
from novel_scraper import NovelScraper  # Importa a classe refatorada
import os
import base64

# Caminhos das imagens
bg_image_path = "assets/bg.png"
gif_path = "assets/typing.gif"  # Nome do GIF salvo localmente

# Função para converter imagens para base64
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_base64 = get_base64(bg_image_path)
gif_base64 = get_base64(gif_path)

# Aplicar estilo CSS para fundo e área central
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');

    /* Fundo da página */
    .stApp {{
        background: url("data:image/png;base64,{bg_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Criar uma área central clara para inputs */
    .center-container {{
        background: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }}

    /* Estilização do título */
    .title-container {{
        margin-top: -30px; 
        text-align: center;
        padding: 10px 0;
        margin-left: 30px;
    }}

    .title-text {{
        font-family: 'Playfair Display', serif;
        font-size: 60px;
        font-weight: bold;
        color: #2C3E50;  /* Cor mais sóbria e sofisticada */
        text-shadow: 4px 4px 10px rgba(255, 255, 255, 0.8), 0px 0px 25px rgba(255, 0, 0, 0.8);
        text-transform: uppercase;
        letter-spacing: 2px;
    }}

    /* Ajuste no contraste do texto */
    h1, h2, h3, h4, h5, h6, p, label, span {{
        color: black !important;
        font-weight: bold;
        text-align: center;
    }}

    /* Centralizar os títulos dos campos de input */
    .stTextInput label,
    .stTextArea label {{
        text-align: center !important;
        width: 100%;
        display: block;
        text-align: center;
    }}

    .stTextInput > div > div > input,
    .stTextArea > div > textarea {{
        color: black !important;
        font-weight: bold;
    }}

    /* Ajustar cor de fundo dos campos de input */
    .stTextInput > div > div {{
        background-color: rgba(200, 200, 200, 0.3) !important;  /* Cinza mais fraco */
        border-radius: 8px !important;
        padding: 5px !important;
    }}

    .stButton > button {{
        background-color: #A9A9A9;
        color: black;
        font-weight: bold;
        display: block;
        margin: 0 auto;
    }}

    /* Centraliza a mensagem informativa */
    .info-text {{
        text-align: center;
        font-size: 20px;
        margin-top: 30px;  /* Aumenta o espaçamento entre o subtítulo e os campos de input */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

components.html(
    """
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            let elements = window.parent.document.querySelectorAll('div[data-testid="stTextInput"] > div > div > div > div > span');
            elements.forEach(el => el.style.display = 'none');
        });
    </script>
    """,
    height=0
)
st.markdown(
    f"""
    <style>
    /* Reduzir e suavizar a mensagem "Press Enter to Apply" */
    div[data-testid="InputInstructions"] > span {{
        font-size: 8px !important;
        color: rgba(0, 0, 0, 0.3) !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Criar um container para o título separado das colunas
st.markdown(
    """
    <div class="title-container">
        <h1 class="title-text">ScrapNovel</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Centralizar o texto informativo
st.markdown('<p class="info-text">Preencha os campos abaixo e clique em <b>Iniciar Scrap</b> para gerar seu ebook.</p>', unsafe_allow_html=True)

# Layout dividido em três colunas
col1, col2, col3 = st.columns([1, 2, 1])

# Coluna 1 (Esquerda) - Placeholder para alinhamento
with col1:
    st.write("")  # Espaço vazio para alinhar o layout

# Coluna 2 (Centro) - Inputs e Botão
with col2:
    # Criando os campos sem um formulário explícito (para evitar a submissão automática com Enter)
    ebook_name = st.text_input("Nome do Ebook", placeholder="Digite o nome do seu ebook", key="ebook_name")
    start_url = st.text_input("URL do primeiro capítulo", placeholder="https://exemplo.com/capitulo-1", key="start_url")
    end_url = st.text_input("URL do último capítulo", placeholder="https://exemplo.com/capitulo-final", key="end_url")
    save_path = st.text_input("Caminho para salvar o ebook", placeholder="Exemplo: C:/Users/SeuNome/Downloads", key="save_path")

    # Botão para iniciar o scrap centralizado
    submitted = st.button("Iniciar Scrap")

# Se o botão foi pressionado, exibir o GIF enquanto o scrap roda
if submitted and ebook_name and start_url and end_url and save_path:
    with col3:
        gif_placeholder = st.empty()
        gif_placeholder.image(f"data:image/gif;base64,{gif_base64}", use_container_width=True)  # Exibir GIF

    # Cria um espaço reservado para a mensagem de status
    status_placeholder = st.empty()
    status_placeholder.info("⏳ Iniciando processo de scrap... Isso pode levar alguns minutos.")
    
    # Inicia o scraper
    scraper = NovelScraper()
    scraper.run_scraper(ebook_name, save_path, start_url, end_url)

    # Substitui a mensagem de andamento por mensagem de sucesso
    status_placeholder.success("✅ Scrap finalizado! Você pode fechar a janela ou iniciar um novo scrap.")
    
    # Exibe log e finaliza GIF
    st.success(f"✅ Ebook **{ebook_name}.docx** salvo em **{save_path}**!")

    log_output = scraper.get_log()
    st.text_area("📜 Log do Scrap", "\n".join(log_output), height=200)

    gif_placeholder.empty()


#st.write("DEBUG: Session State →", st.session_state)  # Mantendo o debug opcional
































