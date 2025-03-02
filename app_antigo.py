import streamlit as st
from novel_scraper import NovelScraper  # Importa a classe refatorada
import os

# Configuração da página
st.set_page_config(page_title="Scrap de Novels", layout="wide")

st.title("Scrap de Novels 📚")
st.markdown("Preencha os campos abaixo e clique em **Iniciar Scrap** para gerar seu ebook.")

# Formulário para evitar recarregamento ao mudar inputs
with st.form("scraper_form"):
    ebook_name = st.text_input("Nome do Ebook", placeholder="Digite o nome do seu ebook")
    start_url = st.text_input("URL do primeiro capítulo", placeholder="https://exemplo.com/capitulo-1")
    end_url = st.text_input("URL do último capítulo", placeholder="https://exemplo.com/capitulo-final")

    # Novo campo para inserir manualmente o caminho de destino
    save_path = st.text_input("Caminho para salvar o ebook", placeholder="Exemplo: C:/Users/SeuNome/Downloads")

    submitted = st.form_submit_button("Iniciar Scrap")

if submitted:
    if ebook_name and start_url and end_url and save_path:
        st.info("⏳ Iniciando processo de scrap... Isso pode levar alguns minutos.")

        scraper = NovelScraper()
        scraper.run_scraper(ebook_name, save_path, start_url, end_url)

        st.success(f"✅ Ebook **{ebook_name}.docx** salvo em **{save_path}**!")

        # Obtendo o log e exibindo no Streamlit
        log_output = scraper.get_log()
        st.text_area("📜 Log do Scrap", "\n".join(log_output), height=200)

    else:
        st.error("⚠️ Preencha todos os campos antes de iniciar.")

st.write("DEBUG: Session State →", st.session_state)  # Mantendo o debug opcional







