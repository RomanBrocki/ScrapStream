import time
import os
from shutil import copyfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from docx import Document
from pattern import pattern
from pattern import replacement
import streamlit as st

class NovelScraper:
    """
    A classe NovelScraper é responsável por realizar o scraping de capítulos de uma web novel,
    compilar o conteúdo extraído e gerar um arquivo eBook no formato .docx.

    Funcionalidades principais:
    - Scraping de capítulos de uma web novel (extração de conteúdo da página).
    - Verificação de CAPTCHA e espera pela resolução manual, se necessário.
    - Criação de eBooks no formato .docx a partir do conteúdo extraído.
    - Registro e contagem de ocorrências específicas no conteúdo da novel.
    """
    
    def __init__(self):
        """
        Inicializa a classe NovelScraper.
        
        Atributos:
        - ebook_name: Nome do eBook a ser gerado.
        - start_url: URL do primeiro capítulo da web novel.
        - end_url: URL do último capítulo da web novel.
        - occurrence_list: Lista que armazena os elementos encontrados no conteúdo.
        - occurrences: Contagem total de ocorrências encontradas.
        - save_path: Caminho onde o eBook será salvo.
        - profile: Caminho para o perfil do usuário do Chrome para o Selenium (necessário para usar cookies e preferências).
        """
        self.ebook_name = ""
        self.start_url = ""
        self.end_url = ""
        self.occurrence_list = []
        self.occurrences = 0
        self.save_path = ""
        self.profile = r"c:\Users\Roman\AppData\Local\Google\Chrome\User Data\Profile Selenium"

    def check_captcha(self, browser):
        """
        Verifica se um CAPTCHA está presente na página e espera que o usuário resolva manualmente.
        
        Este método será executado sempre que um CAPTCHA for detectado, pausando o processo de scraping
        até que o usuário resolva o CAPTCHA manualmente e pressione Enter para continuar.
        """
        while True:
            try:
                captcha = browser.find_elements(By.CLASS_NAME, 'g-recaptcha')  # Procura pelo elemento CAPTCHA
                if captcha:
                    print("Captcha detected! Solve it manually and press Enter to continue...")
                    input("Press Enter after solving the Captcha...")  # Pausa para a resolução manual
                    time.sleep(5)  # Tempo extra para recarregar a página após a resolução do CAPTCHA
                else:
                    break  # Se não houver CAPTCHA, continua o processo
            except:
                break  # Em caso de erro, sai do loop

    def scrape_chapters(self, start_url, end_url):
        """
        Realiza o scraping dos capítulos da web novel, extrai o conteúdo e cria um eBook no formato .docx.
        
        Parâmetros:
        - start_url: URL do primeiro capítulo da novel.
        - end_url: URL do último capítulo da novel.
        
        O método percorre os capítulos da novel, extraindo o conteúdo e salvando-o no arquivo .docx.
        Ele também realiza a substituição de padrões específicos definidos no arquivo `pattern.py`.
        """
        self.start_url = start_url
        self.end_url = end_url
        options = Options()
        options.add_argument("user-data-dir=" + self.profile)  # Usa o perfil do usuário para evitar login repetido
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        # Criação do arquivo .docx para salvar os capítulos
        document = Document()
        document.save(os.path.join(self.save_path, 'Novel.docx'))

        while True:
            browser.get(self.start_url)  # Acessa a URL do capítulo atual
            self.check_captcha(browser)  # Verifica se há CAPTCHA

            try:
                WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'chr-text')))
                title = browser.find_element(By.CLASS_NAME, 'chr-text')  # Título do capítulo
                content = browser.find_element(By.ID, 'chr-content')  # Conteúdo do capítulo
            except:
                print("Error loading page or elements not found. Retrying...")
                time.sleep(5)
                continue  # Se não encontrar os elementos, tenta novamente

            # Abre o arquivo .docx para adicionar o capítulo
            document = Document(os.path.join(self.save_path, "Novel.docx"))
            chapter_text = content.text  # Obtém o texto do capítulo

            # Substitui os padrões definidos em `pattern.py`
            for element in pattern:
                if element in chapter_text:
                    self.occurrence_list.append(f'Found: {element}')
                    self.occurrences += 1
                chapter_text = chapter_text.replace(element, replacement)

            # Adiciona o título e o texto do capítulo ao documento
            document.add_paragraph(title.text)
            document.add_paragraph(chapter_text)
            document.add_page_break()  # Adiciona uma quebra de página entre os capítulos
            document.save(os.path.join(self.save_path, "Novel.docx"))

            # Verifica se o scraping chegou ao último capítulo
            if self.start_url == self.end_url:
                break
            
            try:
                # Tenta encontrar o link para o próximo capítulo
                link = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'next_chap')))
                self.start_url = link.get_attribute('href')  # Atualiza a URL para o próximo capítulo
            except:
                print("Next chapter not found. Stopping...")
                break  # Se não encontrar o próximo capítulo, interrompe o processo

        browser.quit()  # Fecha o navegador após o término

    def get_log(self):
        """
        Retorna um log com todas as ocorrências encontradas durante o scraping.
        
        O log inclui todos os padrões encontrados no conteúdo e o número total de ocorrências.
        """
        log_list = ['List of found occurrences:']
        for occurrence in self.occurrence_list:
            log_list.append(occurrence)
        log_list.append(f'Total occurrences found: {self.occurrences}')
        return log_list

    def save_ebook(self, save_path, ebook_name):
        """
        Renomeia e salva o arquivo .docx com o nome do eBook fornecido.
        
        Parâmetros:
        - save_path: Caminho onde o eBook será salvo.
        - ebook_name: Nome do eBook a ser atribuído ao arquivo .docx.
        """
        self.ebook_name = ebook_name
        self.save_path = save_path
        os.rename(os.path.join(self.save_path, "Novel.docx"), os.path.join(self.save_path, f"{self.ebook_name}.docx"))

    def run_scraper(self, ebook_name, save_path, start_url, end_url):
        """
        Executa o processo completo de scraping e salva o eBook gerado.
        
        Parâmetros:
        - ebook_name: Nome do eBook a ser gerado.
        - save_path: Caminho onde o eBook será salvo.
        - start_url: URL do primeiro capítulo.
        - end_url: URL do último capítulo.
        """
        self.save_path = save_path
        self.scrape_chapters(start_url, end_url)  # Realiza o scraping dos capítulos
        self.save_ebook(save_path, ebook_name)  # Salva o eBook gerado






