from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # Importando 'By' para usar
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from docx import Document
from pattern import pattern, replacement  # Importando pattern e replacement
import time
from config import config  # Importando o config com os seletores

class NovelScraper:
    def __init__(self, config=config):
        """
        Inicializa a classe NovelScraper com um dicionário de configuração.
        """
        self.config = config  # A configuração agora é passada diretamente para o método

        self.ebook_name = ""
        self.start_url = ""
        self.end_url = ""
        self.occurrence_list = []
        self.occurrences = 0
        self.save_path = ""

    def scrape_chapters(self, start_url, end_url):
        """
        Realiza o scraping dos capítulos da web novel, extrai o conteúdo e cria um eBook no formato .docx.
        """
        self.start_url = start_url
        self.end_url = end_url
        options = Options()
        options.add_argument("user-data-dir=" + self.config['profile'])  # Usando o perfil configurado
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        document = Document()
        document.save(os.path.join(self.save_path, 'Novel.docx'))

        while True:
            browser.get(self.start_url)

            try:
                # Espera até que o título do capítulo e o conteúdo estejam carregados
                WebDriverWait(browser, 20).until(EC.presence_of_element_located(self.config['chapter_title']['elemento']))
                WebDriverWait(browser, 20).until(EC.presence_of_element_located(self.config['chapter_content']['elemento']))

                chapter_title = browser.find_element(*self.config['chapter_title']['elemento']).text
                chapter_content = browser.find_element(*self.config['chapter_content']['elemento']).text

            except Exception as e:
                print(f"Error loading page or elements not found. Retrying... Error: {e}")
                time.sleep(5)  # Aguarda 5 segundos e tenta novamente
                continue  # Se não encontrar os elementos, tenta novamente

            document = Document(os.path.join(self.save_path, "Novel.docx"))
            chapter_text = chapter_content

            # Substitui os padrões definidos em `pattern.py`
            for element in pattern:
                if element in chapter_text:
                    self.occurrence_list.append(f'Found: {element}')
                    self.occurrences += 1
                chapter_text = chapter_text.replace(element, replacement)

            document.add_paragraph(chapter_title)
            document.add_paragraph(chapter_text)
            document.add_page_break()
            document.save(os.path.join(self.save_path, "Novel.docx"))

            if self.start_url == self.end_url:
                break

            try:
                # Espera até que o botão de próximo capítulo esteja disponível e clica
                WebDriverWait(browser, 20).until(EC.presence_of_element_located(self.config['next_chapter']['elemento']))
                browser.find_element(*self.config['next_chapter']['elemento']).click()
            except Exception as e:
                print(f"Next chapter button not found or error clicking next: {e}")
                break  # Se não encontrar o próximo capítulo ou não conseguir clicar, interrompe o processo

            self.start_url = browser.current_url  # Atualiza para o próximo capítulo

        browser.quit()

    def get_log(self):
        """
        Retorna um log com todas as ocorrências encontradas durante o scraping.
        """
        log_list = ['List of found occurrences:']
        for occurrence in self.occurrence_list:
            log_list.append(occurrence)
        log_list.append(f'Total occurrences found: {self.occurrences}')
        return log_list

    def save_ebook(self, save_path, ebook_name):
        """
        Renomeia e salva o arquivo .docx com o nome do eBook fornecido.
        """
        self.ebook_name = ebook_name
        self.save_path = save_path
        os.rename(os.path.join(self.save_path, "Novel.docx"), os.path.join(self.save_path, f"{self.ebook_name}.docx"))

    def run_scraper(self, ebook_name, save_path, start_url, end_url):
        """
        Executa o processo completo de scraping e salva o eBook gerado.
        """
        self.save_path = save_path
        self.scrape_chapters(start_url, end_url)
        self.save_ebook(save_path, ebook_name)








