# config de profile, elementos dá pagina e ações correspondentes
from selenium.webdriver.common.by import By

config = {
    'profile': r"c:\Users\Roman\AppData\Local\Google\Chrome\User Data\Profile Selenium",  # Caminho do perfil do Chrome

    'chapter_title': {
        'elemento': (By.CLASS_NAME, 'chr-text')  # Seletor para título do capítulo
    },
    'chapter_content': {
        'elemento': (By.ID, 'chr-content')  # Seletor para conteúdo do capítulo
    },
    'next_chapter': {
        'elemento': (By.ID, 'next_chap')  # Seletor do botão de próximo capítulo
    }
}

