# config de profile, elementos dá pagina e ações correspondentes
from selenium.webdriver.common.by import By

config = {
    'profile': r"c:\Users\Roman\AppData\Local\Google\Chrome\User Data\Profile Selenium",  # Caminho do perfil do Chrome
    'author': 'ScrapNovel',  # Autor do eBook
    'chapter_title_selector': (By.CLASS_NAME, 'chr-text'),  # Seletor para título do capítulo
    'chapter_content_selector': (By.ID, 'chr-content'),  # Seletor para conteúdo do capítulo
    'next_chapter_selector': (By.ID, 'next_chap')  # Seletor do botão de próximo capítulo
}


